---
title: "Efficient vim editing: Don't use visual mode if possible"
date: 2023-08-14T18:44:18+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: true
description: "Visual selected and then yank? Why don't you just yank the text object?"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

Efficient tips for you, the beginers vimers.

# why?
because it has the same effect, but visual mode have more keys storke

If you often use visual mode before yank or delete text, you should take care, you may be in situation of inefficient editing.

# Operator-pending mode vs Visual mode
Operator-pending mode are mode when vim is waiting your **motion**. What is **motion** in vim? **Motion** means the range of text you would like vim to apply the command. *This range* can be `w`, `iw`, `e`, or `i{`. In another words, **motion** means the region of selection. The **motion** I have just mentioned control how the region of text will be applied by the command. Like `d` in `diw`.

Visual mode, similiar to drag your mouse selecting random region, for vimers, we usually selected by keyboard, We will be involved to visual mode first, either by `v`, `V` or `<C-v>`, then you move your cursor to select the region you want. Similiar to Operator-pending mode, right? But we take a look how much key you have pressed.

```text
Here is the example text:

local M = {
    local function doSomething(x, y)
        local x, y = x, y
        return x * y
    end
}
```
We assume you want to delete the text inside M. If you prefer visual mode.
![./img/visual-mode.gif](img/visual-mode.gif)
the key sequence: `vi{x`

If you prefer Operator-pending mode.
![./img/omode.gif](img/omode.gif)
The key sequence: `di{`

You will save one key by the end. Actually, if you prefer first enter visual-mode, it may be the inertia from using other GUI application with mouse. But remember you don't have to keep such practice in vim, you can directly delete or yank with **motion**. It may be little save in once. However, if you are preparing to use vim for future, you should keep upgrading your editing style smoother. Leverge Operator-pending mode is basic practice for efficient editing.
