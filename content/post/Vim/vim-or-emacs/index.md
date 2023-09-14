---
title: "Things to consider before switch from Vim to Emacs"
date: 2023-09-14T12:49:55+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Things to consider before switch from Vim to Emacs"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

Is emacs evil the another Lisp based Vim?

I love tweaking the editor, though it is meaningless. I recently finish the merging from Vim to Neovim, mainly because the plugin [tree-sitter](https://github.com/nvim-treesitter/nvim-treesitter) so to make such switching. Just because making the editor prefect my wired behaviour is suffer, I have to read tones of docs just to discover if there is already some API allow me to do so. Before the Neovim become stable, I have played with Emacs a little bit(Purely treat it as toy, haven't do any editing with it). I just find that emacs seem to be similiar to Vim after the plugin [evil](https://github.com/emacs-evil/evil) is installed. Though Emacs has disappeared in my editor list, since I know I am trying to convert Emacs becoming the second Vim.

After try to get with emacs serval more times, I discover the reason I can't get fluent in Emacs as in Vim even with the help of Evil.

Although I have seen many discussion after evil or vim, some claims that the editing feeling in Evil is same as vim. This is only partial correct. Undoubly the editing style is the best clone of Vim among all vi-emulation. But you should care it is vi-emulation but not vim-emulation. When you use vim, are you only using the vi key bindings? Probability not, you are as well as using the vim-style tab completion, Vim UI, vim command and vim ecosystem. In other wrods, there is really different between the Vim way and Emacs way.

The next point, the difference between GUI application and TUI application. Emacs has more advanced package that help you "live in Emacs", where GUI seems to be a better choice than Terminal one in order to discover its full power. On the other hands, Vim is merely a Editor, not many will suspose it did more outside the scope of editing, so Terminal version is usually enough for most of the use case of Vim. However, this huge difference will affact how much you can accept the switching from TUI to GUi application. If you use a lot terminal application, Vim of course is more nature way to use with. However, if a terminal emulation inside editor is enough for you, switching to new editor will be much easier, since you don't have to re-shape your workflow entirely.

The ecosystem of Vim and Emacs. The most important point everyone who want to switch from Vim to Emacs should know, Vim plugins are design for vim key bindings user, while Emacs plugins are not intended for evil key bindings user, you will have to do a lot remaps just to make it the vi way. If all you need is editing, you don't have to switch, because in my experience, it is all about finding an alternative plugins in Emacs. As I say, it is converting Emacs into Vim. When you want to add editing feature to evil-mode, you either have to pay if there exist a solution or you write it your own, I don't know how great the community of evil-mode is compare to Vim's. It is just higher probability that you will find implemented solution in Vim's community when talking about extend vi editing capability.
