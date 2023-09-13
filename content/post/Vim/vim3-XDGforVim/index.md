---
title: "XDG base configuration for Vim"
date: 2023-08-03T09:11:30+08:00
# weight: 1
# aliases: ["/first"]
tags: ["vimrc"]
author: "sokinpui"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Simple hack to have XDG based configuration for Vim"
canonicalURL: "https://canonical.url/to/page"
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

I have seen some post and issue on Vim github that want XDG base configuration become one of the runtimpath of Vim(not Neovim), actually a simple hack can done so.
```sh
mkdir $HOME/.config/vim
mkdir $HOME/.vim
mv $HOME/.vimrc $HOME/.vim/vimrc
mv $HOME/.vim $HOME/.config/vim 
ln -s $HOME/.config/vim $HOME/.vim
```
Do you know there your `vimrc` can located at either `$HOME/.vimrc` or `$HOME/.vim/vimrc`, so you can move your whole runtimpath to `$HOME/.config/vim`, then create a symbolic link `$HOME/.vim` point to `$HOME/.config/vim`.

Although I know XDG is more than just a directory, it may still be helpful for group all your configuration together.

