---
title: "Kmonad"
date: 2023-08-09T16:51:55+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Remap keyboard with kmonad"
canonicalURL: "https://canonical.url/to/page"
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

# What is kmonad?
[kmoand](https://github.com/kmonad/kmonad):
> KMonad is an advanced tool that lets you infinitely customize and extend the functionalities of almost any keyboard.

You can create layer, remap keyboard keys, make a [colemak](https://colemak.com/) on qwerty layout keyboard, create [home row modifier](https://precondition.github.io/home-row-mods), or record keyboard macros.

Since it is a software, you don't have to complie QMK or buy a new keyboard that support recomplied. BTW, I haven't felt laggy when using kmonad, it works both on X11 and Wayland.

## Install kmonad
The official repo recently support download directly from package manager of Arch Linux, GNU Guix and Void Linux. Non of this is my using distro, so I complied it from source with its [tutorial](https://github.com/kmonad/kmonad/blob/master/doc/installation.md#using-stack).

First we need to clone the repo, then change directory into the cloned repo, finally build it with haskell build tools **stack**, if you haven't install stack, you need to first install it.
```sh
git clone https://github.com/kmonad/kmonad.git
cd kmonad
stack install
```
Now you can test if it has successfully installed.
```sh
kmonad
```
Kmonad has a lot of feature you can leverge with, in this blog, I will only introduce features that will be used in tmux. For more details you can check its [official tutorial](https://github.com/kmonad/kmonad/blob/master/keymap/tutorial.kbd) or [tutorial on youtube](https://www.youtube.com/watch?v=Dhj1eauljwU&t=199s&pp=ygUGa21vbmFk)
## KMonad how
Snippet from kmonad configuration file: (keymaps of 100% keyboard)

```lisp
(defsrc
  esc  f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12  pause del  home end  pgup  pgdn 
  grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc       nlck kp/  kp*  kp-
  tab  q    w    e    r    t    y    u    i    o    p    [    ]    \          kp7  kp8  kp9  kp+
  caps a    s    d    f    g    h    j    k    l    ;    '    ret             kp4  kp5  kp6
  lsft z    x    c    v    b    n    m    ,    .    /    rsft up              kp1  kp2  kp3  kprt
  lctl lmet lalt           spc            ralt cmp   rctl left down rght       kp0  kp.
)
```
