---
title: "Efficient Vim: try not to overwrite vim default keybindings."
date: 2023-08-19T21:20:53+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Try to stand with Vim default key bindings!"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

We know Vim is known as its extentability, why would I recommend you stop making your own configuration? Because it comes with cost.

# The issue
You find `cw` is difficult to type, you find that `cl` is overlapping with `s`, you add some remap to your `vimrc`:
```vim
onoremap l w
onoremap L W
onoremap h iw
onoremap H iW
```
Indeed, this is how I used to use vim. ( [link to post]({{< ref "post/vim8-useful-keymap/index.md#text-object" >}}) ). The keybindings help me, but just so little improvement. Just like other vimers, I tends to use vim style in other application like zsh, Emacs, obsidian and tmux etc. When I sit down and going to work hard, I find the keybindings on them are just wrong, I forget to sync my config on Vim to other application, I have to find solution for each application, luckly, those application is say to be easy to config with their vi-mode. While I can't make sure current situation can apply to future, I can't promise I stil using same set of tools or using the same vim config. The more application I use, the more time I have to spend on finding solution in other to make the application prefectly fix my using case.

I am afraid If I having too much personalization, I would loss the vim compability from any vim emulation one day. One reason keep me using vim is that  there is vim-emulation everywhere, Once I have learn the keybindings, I can keep the same workflow no matter the tools. Therefore, I stop overwriting vim default keybindings. Remapping I use currently are mostly related to plugins, and is trigger by leader key.

# Outside Vim, the keyboard layout, the cose of too much personalization
The keyboard layout I current I use are my own personalized version, it is build on QWERTY, but I have some change with modifiers, I have made `space` as sapce-shift(tap as space, held as shift), shift when held, I have made `left shift` as esc-ctrl, make some changes wiht special symbols, turn `caps lock` become layer raiser, `{`, `}` `[` and `]` are `caps lock` + `kjiu`. Since those key are highly related to vim motion, my editing and typing speed are dropped significantly when I use any vanilla QWERTY keyboard, inside and outside Vim. Especially `shift` is mapped to `space`, there are just so many vim motion require capital letter or symbols `!@#$%^&*(` to use. I afraid if one day I have to use some public workstation, I may just stand in front it, type like those who use computer first time.

To change your keyboard layout, either via software( karabiner elements on Mac, xinput on linux ), or via hardware. I haven't touch my Macbook since I have upgrade my keyboard layout on a second hand thinkpad. One of the reason are the keyboard layout on two machine have a huge different after upgrade, since the software used are different on Mac and Linux, I don't want to spend extra day config Macbook just to sync the layout.

Or I can purchase a complible keybord to have the universal layout on different mahcine. Nevertheless, they are expensive and I still need to bring my laptop work outside physical keyboard may not be a good choice.
