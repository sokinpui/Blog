---
title: "Ctrl-c Ctrl-v copy and paste in tmux and zsh"
date: 2023-08-04T12:50:18+08:00
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
description: "Use Ctrl-c adn Ctrl-v to copy and paste in tmux and zsh under Linux terminal"
canonicalURL: "https://canonical.url/to/page"
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

If you use neither window Nor mac os, you may find you cannot use Ctrl-c to copy and Ctrl-v to paste in terminal. You have to press `Ctrl-SHIFT-c` to copy selected items, and `Ctrl-SHIFT-v` to paste from system clipboard.

Window user don't have to concern this issue, because I believe you will endup with wsl, which by the end is close to Linux env. <br>
Mac user don't need to concern this issue, because you can use `CMD-c` and `CMD-v`.

# Ctrl-c to copy in tmux copy mode
add those line to your tmux.conf, and source it.
```tmux
set -g mouse on
setw -g mode-keys vi
bind -T copy-mode-vi C-c send-keys -X copy-pipe-and-cancel "wl-copy" copy-selection-no-clear
bind -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-selection -x copy-selection-no-clear
```
`wl-copy` is for Wayland user, If you are Xorg user, change `wl-copy` to `xclip`. Of course, you have to download this package from your package manager first. The last line enable mouse drag to select region, it is no-sense to disable mouse if you are going to use `Ctrl-c` to copy.

# Ctrl-v to paste in zsh
add this line to your .zshrc and reopen zsh to see the effect.
```sh
bindkey '^V' _paste-copy-using-xsel # Paste from clipboard
```

# The reason don't remap in terminal
remap ctrl-c in terminal is dangerous, you may neither able to cancel nor stop process in terminal. What's more, mapping in tmux and zsh make sure the protablility of your env, they can be reproduce in any terminal, that is the reason I use tmux for tab in terminal instead of they tab function of terminal, even I am using kitty terminal which support tab and session.

# What does Ctrl-c do in terminal?
Ctrl + C is used to send a SIGINT signal, which cancels or terminates the currently-running program. The reason Ctrl-c is use to stop program is historic reason. Here is an [answer](https://unix.stackexchange.com/a/245574/566291) posted by StackOverflow user **Gilles 'SO- stop being evil'**:

> The “kill” meaning of Ctrl+C is very old, I think even older than Unix. Wikipedia traces it back to TOPS-10, which would date it from the late 1960s. The article explains why Ctrl+C was a reasonable choice: in ASCII, which was published in 1963, the corresponding character is ETX, end-of-text. Lacking a character meaning “stop”¹, a character meaning “this segment of input is over” was a reasonable choice to mean “stop the current processing”.
> 
> The “copy” meaning of Ctrl+C comes from Xerox PARC, the inventors of copy-paste in its modern form (and most other fundamentals of graphical user interfaces). I don't know exactly when that was, but it must have been the late 1970s. This thread on User Experience Stack Exchange discusses the choice of key bindings; C for copy makes a lot of sense.
> 
> There was little reason for PARC to reject Ctrl+C for copy on the basis of the existing meaning in TOPS-10 and Unix terminals. Operating systems and applications were more diverse then, and far fewer people used computers; there was no opportunity nor call for a single standard for key bindings across all applications. Other uses for Ctrl+C in popular applications include page-down in WordStar² and mode-specific command in Emacs. All of these were designed independently, for applications with often different requirements, running in different environments.
> 
> You can configure the terminal key bindings with the stty command. The terminal bindings are active when the terminal is in cooked mode³. For example the command stty intr ^G sets the character that sends a SIGINT signal to Ctrl+G instead of Ctrl+C. The ^G character is BEL in ASCII; when sent to a terminal, it means “ring the bell”. It's the character that Emacs uses for “interrupt the current operation” (rationale: the application sends BEL to the user via the terminal to interrupt the user; the user sends BEL to the application via the terminal to interrupt the application). It doesn't have a standard meaning when sent to a terminal.
> 
> Most shells provide line editing features, so they set the terminal to raw mode. So do full-screen text mode applications. You may need to configure these applications to recognize Ctrl+G instead of Ctrl+C, and some may have non-configurable key bindings. So changing the interrupt character may or may not be practically doable depending on which applications you use.
> 
> Another approach could be to configure your terminal to change the byte sequence that it sends for the Ctrl+C keychord, or make it send nothing and instead perform a copy operation. You would also choose a different keychord to send Ctrl+C (if you have a non-laptop PC keyboard, you could use the out-of-the-way Pause/Break key). Not all terminals can be configured in this way.
> 
> ¹ Ctrl-S (XOFF) means stop, but it's addressed to the terminal, not to the application. <br>
> ² Next to Ctrl+X for next-line, with Ctrl+E and Ctrl+R for previous-line and page-up; these keys were chosen due to their placement on a QWERTY keyboard. <br>
> ³ Nitpick: cooked mode is a set of terminal settings, including the interpretation of several characters including one that sends an interrupt signal.

# What does Ctrl-v do in
The CtrlV key often meant "verbatim insert" – that is, insert the following character literally without performing any associated action. 
example
```text
typing |
press Ctrl-v and then press backspace
typing <BS>|
```
