---
title: "Addictive configuration, the endless tweakings to prefect"
date: 2023-09-01T13:39:05+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Prefect workflow is about 1% efforct and 99% tweaking"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

Holy configuring time. Tweaking whatever, editor, notes app, keyboard, shell, OS, browser extension, information system, and some new concept like second brain, roam-like backlink information system. Wow, there is a lot to play with, so that we can do nothing and config them all the time!

# CONFIG EDITOR
Editor with infinite extendibility like Neovim, Emacs is extremely addictive. Both of them come with their own scripting language, so that you can do "editor programmimg", make it the way you like, make it to prefectly fit your workflow and strange needs. Especially eamcs, there exist so much packages that can help you "live in Emacs". Nevertheless, you can choose not to. Neovim in other hand, has less feature than Emacs, but still very configurable. Time is very easy gone when try some new package or new feature. Sometimes I just want to add some plugins for my neovim, after install it. I decide to spend "some time" to read the documents, but turn out I have spent whole afternoon finding some special API to change the plugin to the way I want to.

# CONFIG TERMINAL
If you are Mac and linux user, you should have known an app GUI application called "Terminal", it is another time-sink. First, we have to choose a terminal. If I use many Temrinal application, I would consider replacement for the system given one. After that, I have to config the font, color scheme so that it is usable. Still not yet finished, You have to had a handy shell, you should choose one from some common shell like fish, zsh, or bash. You have to spend extra time to make the shell usable, it will take longer if you choose zsh and bash, since you will have to know many tecnical terms like "zle", "precmd_functions", "LBUFFER", "setopt", ... There are so much required knowledge if you really want to make zsh and bash into "your shape". Oh GOD, already spending a week of time? If you want to have mutliple tabs opened, so that convient youself to have many cli application progess at the same time, you should either pick **tmux** or functionility provided from the terminal you pick. If the temrinal you pick is alacritty, then you have no choice, you are forced to use **Tmux**. If you are fine to use mouse to create and navigate tabs with you GUI temrinal, you can do less. If you prefer keyboard-driven, then you have to spend extra time just for creating your own style shortcut key. If you choose to accept the default keybindings. Either of them suck, because you will find the default key bindings conflict with other hot keys of cli tools like emacs or vim, or you will realized that they are not designed for human(Tmux). Yet, if you want to leverge terminal and shell to automate your workflow, you should spend even more time to learn the scripting language sh. Bash, Zsh, and Sh are POXIS compabible shell, you knowledge can be used in other shell. If you are used to Bash but decide to use Fish, you will have to learn the new language(actually new style, basically python-like). AHHHHH, everything should be done, right? you still lacking the interface to interact with your os, they are the tones of command line tools, some of them sed, ls, cd, z, rm, mv, cp. With every tool have their unique set of options( so call flags, althoug the name of flags follow some pattern, I guess you still don't want to remember all of them ). After all, you have your environment prepared, and finally able to start your work? Definitly not, still too many to config!

# CONFIG DESKTOP ENVIRONMENT
Desktop environment is the sand box to contain all your configurable tools, where itself is another tweakable stuff. The crazier one is window manager, like i3, hyperland, dwm. If you don't know what is window manager, you can go to [/unixporn](https://www.reddit.com/r/unixporn/) have a quick look, those fancy binary split window are managed by window manager. You have to write your own config file or copy from others. However, if you want to "make it fit your workflow better", you are better understanding what are in your config file, yet extra time have to spent. I personally prefer Desktop environment like gnome, kde and xfce. I don't have crazy many window popup anytime, most of the time the window are fixed in some places, gnome extension [gtile](https://extensions.gnome.org/extension/28/gtile/) already cover most of the use case. But when I start personalizing gnome ( I don't want the top bar appear, I have a small laptop screen ). I still unavoidly need to tweak a little bit. Embarssingly, I find gnome is not portable, when I move to new machine, I have to config gnome again( I will find the solution to prepare for future merging ).

# BUILD INFORMATION SYSTEM
Wow, wow, wow, to build information system is never an easy task. You need a good editor, either have good extension support, or originally built for information processing. Otherwise, you need to spend some time to find the best solution for collecting, grouping, manage and organize information into useful knowledge. It is really hard to find one application can do all of them. All-in-one solution like Notion works very well with chart data, while it don't have a decent editor as powerful as vim or emacs( it don't support vi mode! ). Some general purpose editor like emacs, though it has gui version that can render rich content, but its UI is hard to battle with Other domain specify gui application. In other words, you can make the UI as beauty as them of course, but it require time and quite useless. Eventually, to have a prefect information system, the hardest part is how you can connect all discrete application together to do useful stuff and keep it forward. If you system is not robust enough to fit your future requirement, how should you handle?

# CONSISTENT HOT KEYS
Consistent hot key style anywhere is difficult, if you are vi-mode fever, I guess You will want to use vim everywhere, because it is the reason you live on the earth. Your blood is flowing in your body with hjkl(is hjkl really the most amazing magic of vim? But not text object and modal editing? Why so many recommend vim because you can use hjkl to replace your arrow key! ). However, seriously, outside text editing, is vi-mode still have the magic? Is it really better than mouse and keyboard shortcut? Nevertheless, it is a personal choice. The only things I can ensure, it is difficult to maintain many vi-mode on many non-vim application with personalized config.

# Reailty of config
Configuration most of the time grow up naturally, new feature is used only when you need this, I believe nobody will spend a month merely try to make your workflow and tools to be prefect. You leverge the old feature, find another way that can smooth you workflow, then you learn it, try it, love it. That how config should be. It grows from day to day, my current config do not appear suddenly, I add a few lines each time. So eventually I don't feel that I have spend crazy amount of time for config.

Yet I don't feel that I have spent many time on config, I actually spend lot of time **playing** with those configurable "toys". TASTING THE UNKOWN FEATTURE IS FUN, ISN'T IT? It is hard to describe the feeling. Imagine you build an axes with LEGO( config ) and try to cut down a tree(real world task) ... and it works ... AMAZING!

