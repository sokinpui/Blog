---
title: "Tmux key bndings less suffer"
#description: <descriptive text here>
date: 2023-07-15T17:34:00+08:00
draft: false
toc: true
image: ""
tags: ["tmux"]
categories: []
---

Do you use tmux? Do you think the default key bndings of tmux unacceptalbe? Here are some tips I have collected.

# TIPS
## 1: Skip prefix
After change some key bndings like prefix from `C-b` to something like `C-space`, you may still find annoying to press prefix for some handy shortcut like switching windows.
To skips the needs of prefix, you may add the option `-n` before the command <br>
To switch windows without prefix using `M-n` <br>
```
bind -n M-n select-window -t :+
```

## 2: Keyboard Macros
Macros are collection of keys sequence, you may find some key on your keyboard is less used like `right alt`, then you can convert this key as tmux specify modifier key, press this key will do a sequence of shortcut. To achieve this, you may need a key mappings application, on Linux I recommand [kmonad](https://github.com/kmonad/kmonad); on Macos, I recommand [Karabiner elements](https://karabiner-elements.pqrs.org/). If you use karabiner elements, use [goku](https://github.com/yqrashawn/GokuRakuJoudo) to configure Karabiner elements JSON file easier, life saver!

## 3: open new window under current directory
It is especially great working on small screen laptop, if you spawn new pane, then you are in the same directory, however, if you spawn a new window, you will by default at `$HOME`. <br>
You can use <br>
```
bind -n M-o new-window -c "#{pane_current_path}"
```
to map `Alt-o` to open new window udner current directory.
