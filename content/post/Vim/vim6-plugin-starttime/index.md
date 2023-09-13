---
title: "Neovim plugins: vim-startuptime, make startup time information readable"
date: 2023-08-04T15:23:09+08:00
# weight: 1
# aliases: ["/first"]
tags: [""]
author: "sokinpui"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Desc Text."
canonicalURL: "https://canonical.url/to/page"
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

You can check the startup time of Vim/Neovim by add the option `--startuptime <name of log file>`, however meaningful information is difficult to find Maybe you may want to find the plugin that affect startup time most significantly, but lost in tones of numbers and lines. This plugins make testing and viewing startuptime log easier.
![vim-startup](vim-startup.png)

# Plugins: [vim-startuptime](https://github.com/dstein64/vim-startuptime)
Screenshot:
![demo](plugin.png)
This plugins allow you check the startup time afte open Neovim, maybe more intutitive than using option `--startuptime`?

