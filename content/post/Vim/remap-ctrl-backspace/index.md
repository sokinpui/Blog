---
title: "[Vim/Neovim] Mapping Ctrl+Backspace in Vim"
date: 2023-09-17T20:47:03+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

Don't you note that remapping of <C-BS> have not effort? Instead, you should use <C-H>.
```vim
inoremap <C-H> <C-w>
cnoremap <C-H> <C-w>
tnoremap <C-H> <C-w>
```

You can check the keycode in temrinal with `showkey -a`
![./img/c-bs.gif](img/c-bs.gif)
