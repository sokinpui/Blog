---
title: "Try to find the least key solution to navigate up and down in Vim"
date: 2023-08-18T13:14:48+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Try to find the least key solution for vertical motion in vanilla Vim"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

> update at Sat Aug 19 03:24:56 PM CST 2023

TL;DR, I find my blog is too verbose, let me summarize it.

I am try to find the least key solution to jump within certain numbers of lines, that is
Assume we map J and K to <n>j and <n>k respectively, for example, `nmap J 5J`
$$
lines = a \times n \times j/k + b \times j/k
$$

We want the $min(a+b)$ among the $n$ we test.

---

In this blog, I am try to navigate up and down using `<c-d>`, `<c-u>`, the remapped `J` and `K`, they are remapped to `<x>j` and `<x>k` respectively. And jk of course.

# Why this blog?
I know there is tons of ways I can perform in vertical motion, like plugin [leap.nvim](https://github.com/ggandor/leap.nvim), [flash.nvim](https://github.com/folke/flash.nvim), using `/` or `?` to searching, or using fuzzy finder tools like [fzf.vim](https://github.com/junegunn/fzf.vim) or [telescope.nvim](https://github.com/nvim-telescope/telescope.nvim). I just want to keep a habit or in another terms, I would like to find a method that can extend my muscle memory to any vanilla vim emluation without too much configuratione.

# The problems
I have to move up and down to get my cursor right one some words, sometimes, the words just appear too many times, searching is useless. I don't want to move my hand to get my mouse clicking at that position when I know that I can use just a few keys to get here.

# How I try to solve

1. H to the top of the screen
2. M to middle of the screen
3. L to the bottom of the screen
4. `<c-d>` and `<c-u>`
5. nmap J 5j (4j, 6j, or whatever)
6. nmap K 5K (4K, 6K, or whatever)
7. j and k

I try to use `<c-d>` and `<c-u>` to move half page up and down, they are vim default key bindings. Moreover, they are widely supported by any vim emluation and vanilla vi on random remote server. Use J and K to make a smaller steps, and finally use j and k to move to the lines I want.

But..., how should J and K mapped? 4j, 6j or 5j? Indeed, I write this blog is to share a short snippets that aims to find the best solution.

The way to navigate is similiar to binary search algorithm, we use the big steps like `H`, `L`, `M`, `<c-d>` and `<c-d>` jump to the location around the target. Then we use `J`, `K`, `j` and `k` to move subtlety.

So, we need to find the less key solution to map J and K in order to get to any lines in screen. The least average jumps needed will be the ideal J and K seeking for.

However, the problems can be simplify to how to use the less key to move within quarter of page. We can mapped H and L to jumps to the upper quarter and lower quarter of the screen, and it is easy.
```vim
nnoremap H <Cmd>set scrolloff=0<CR>H10gj<Cmd>set scrolloff=8<Cr>
nnoremap j <Cmd>set scrolloff=0<CR>J10gh<Cmd>set scrolloff=8<Cr>
```
Set scrolloff=0 to ensure H and L will jump to top and bottom of screen, then we move <n> lines down/up, in my case it is 42 // 4 = 10, 10 lines down will jumps quarter of screen.  lastly we set back our scrolloff, in my case, it is 8.

Now, we only need to find the least key to move within quarter of screen.

To find how JK should be mapped, we can find the average number to move from 1 lines to 10 lines with different JK mapped.

here is the snippets I use to find the best JK:
```python
jumps_range = 10

for jump in range(2, jumps_range):
    count = 0
    for lines in range(1, jumps_range):
        count = count + lines // jump + lines % jump
    average = count / jumps_range
    print("average jumps needed for JK mapped to", jump, "is", round(average, 2))
```
and the result is:
```text
average jumps needed for JK mapped to 2 is 2.73
average jumps needed for JK mapped to 3 is 2.27
average jumps needed for JK mapped to 4 is 2.27
average jumps needed for JK mapped to 5 is 2.45
average jumps needed for JK mapped to 6 is 2.73
average jumps needed for JK mapped to 7 is 2.82
average jumps needed for JK mapped to 8 is 3.09
average jumps needed for JK mapped to 9 is 3.55
average jumps needed for JK mapped to 10 is 4.18
```
And we can see, the least key is 3 or 4. Then I add those lines to my `.vimrc`
```vim
noremap J 4j
noremap K 4k

nnoremap H <Cmd>set scrolloff=0<CR>H11gj<Cmd>set scrolloff=8<Cr>
nnoremap L <Cmd>set scrolloff=0<CR>L11gk<Cmd>set scrolloff=8<Cr>
```

Or if H and L is too complex and may note copied to other vim emluation, you would like to only use `<c-d>`, `<c-u>`, the `jumps_range` can be 21. (21 is half of my screen).

After modified `jumps_range` to 21, the result is:
```text
average jumps needed for JK mapped to 2 is 5.24
average jumps needed for JK mapped to 3 is 4.0
average jumps needed for JK mapped to 4 is 3.57
average jumps needed for JK mapped to 5 is 3.52
average jumps needed for JK mapped to 6 is 3.57
average jumps needed for JK mapped to 7 is 4.0
average jumps needed for JK mapped to 8 is 4.0
average jumps needed for JK mapped to 9 is 4.29
average jumps needed for JK mapped to 10 is 4.86
average jumps needed for JK mapped to 11 is 5.24
average jumps needed for JK mapped to 12 is 5.29
average jumps needed for JK mapped to 13 is 5.43
average jumps needed for JK mapped to 14 is 5.67
average jumps needed for JK mapped to 15 is 6.0
average jumps needed for JK mapped to 16 is 6.43
average jumps needed for JK mapped to 17 is 6.95
average jumps needed for JK mapped to 18 is 7.57
average jumps needed for JK mapped to 19 is 8.29
average jumps needed for JK mapped to 20 is 9.1
```
And we can see, 5 is the best in this case.
