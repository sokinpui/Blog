#!/bin/env python
"""
Syndicate Medium Posts

Following the API documentation:
https://github.com/Medium/medium-api-docs/tree/69c4cdb894e74ac7710572f9a34bc2421a8def2e

"""
import json
import subprocess
import time

from http.client import HTTPSConnection
from urllib.parse import urlparse

import frontmatter

AUTHOR_ID = "@sosokinpui"

def syndicate_post(post):
    """
    Takes a blog post and syndicates it to Medium
    """
    # Grab secret
    medium_secret = "2bb106e84e00aa42a788ef5c14135975ba6aabbc622ac432da51c25cd61cd61c1"

    # Structure API Request
    blog_post = dict(
        title=post['title'],
        contentFormat="html",
        content=post['content_html'],
        tags=post['tags'],
        canonicalUrl=post['url'],
        publishStatus="public",
        license="all-rights-reserved",
        notifyFollowers=False # TODO: Temporary while refreshing content
    )
    request_headers = {
            "Host": "api.medium.com",
            "Authorization": f"Bearer {medium_secret}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Accept-Charset": "utf-8",
    }

    # Send Request
    conn = HTTPSConnection("api.medium.com")
    conn.request(
        "POST",
        f"/v1/users/{AUTHOR_ID}/posts",
        json.dumps(blog_post).encode("utf-8"),
        request_headers
    )

    # Check and parse response
    response = conn.getresponse()
    if response.status != 201:
        raise Exception(f"Medium API rejected the request with response code {response.status}")
    medium_response = json.loads(response.read().decode('utf-8'))
    conn.close()

    return medium_response

def update_front_matter(post, medium_data):
    """
    Take the medium response object and encode
    the unique identifier back to the blog post.
    """
    # Figure out path of file
    ORIG_URL = urlparse(post['id'])
    file_path = "content" + ORIG_URL.path[:-1] + ".md"

    # Read existing frontmatter and edit the post id
    item = {}
    with open(file_path, "r", encoding="UTF-8") as content_file:
        item = frontmatter.load(content_file)
        item['medium_post_id'] = medium_data['data']['id']
    
    # Write out new frontmatter
    with open(file_path, "w", encoding="UTF-8") as content_file:
        content_file.write(frontmatter.dumps(item))
        
if __name__ == "__main__":
    # Generate the necessary feed files
    subprocess.run(['hugo'], check=True)

    # Grab blog's feed
    data = ""
    with open("public/blog/index.json", "r", encoding="UTF-8") as feed_file:
        data = feed_file.read()
    feed_data = json.loads(data)

    # Go through each post and check syndication status
    for post in feed_data['items']:
        medium_enabled = post['_syndication']['medium']['enabled']
        medium_post_id = post['_syndication']['medium']['post_id']
        if medium_enabled and medium_post_id is None:
            # Syndicate.....
            print(f"Syndicating \"{post['title']}\"")
            medium_result = syndicate_post(post)
            update_front_matter(post, medium_result)
            print(medium_result['data']['url'])
            time.sleep(60)
