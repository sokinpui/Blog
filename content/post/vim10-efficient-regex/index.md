---
title: "Efficient vim editing: master regular expression"
date: 2023-08-15T12:34:25+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: true
hidemeta: false
comments: true
description: "Use regular expression when it do the best"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

When will be used in editing?

# Learn regular expression
regular expression, usually shorten in **regex**. Not only helpful inside Vim, heavily used in bash script, and any thing related to text stream editing. Regex provide rules to abstract text. As a editor user, most of the time is working with text, master such rule will be handy. Use regex smart can reduce the need of repeitive editing, and hence improve the productivity.

# Use regular expression in Vim
There are serveral case you will use regualar expression
1. search `/`
2. `:s/`
3. `:g/`
4. `:vimgrep`
5. `:grep`

----------------------------------------------------------------

setting visual the regex you type: increment search
`set insearch`

a-zA-z0-9_

special characters
```text
(){}[].*+!#@%^&*\|$"'<>/-
```

grouping
\(\) \1 \2 \3

magic option

use case and demo
