---
title: "Kmonad"
date: 2023-08-09T16:51:55+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: true
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
Kmonad use lisp-like language to configure. The name of the key buttons should not longer than four words except `pause`
{{< details "meanings of key names" >}}
`cmp` = fn modifier

`ctl` = control modifier

`met` = meta modifier ( windows key on your keyboard )

`alt` = alt modifier

`sft` = shift modifier

`lalt` = left alt modifier

`ret` = return

`bspc` = backspace

`grv` = ~

`caps` = caps lock
{{< /details >}}

## config kmond
### first block
First, create a file `config.kbd` (arbitary name you want with extension `.kbd`)
```sh
vim config.kbd
```
The first block in your config is details about the keyboard you want to modify.
```lisp
(defcfg
  input  (device-file "/dev/input/by-path/pci-0000:00:14.0-usb-0:4:1.0-event-kbd")
  output (uinput-sink "100 keyboard")

  fallthrough true
  allow-cmd true
)
```
The first two line are necessary, you can check input keyboard at `/dev/input/by-path/`. To find the name, you can unplug and then replug your keyboard, The line disappear and appear will be target keyboard. then pass it to the function `(device-file "/dev/input/by-path/<your-keyboard-path>)`

The second line outpu will use uinput, "100 keyboard" is the description that pass to uinput.

The remain two line are optional.

When `fallthrough` is true, unmatched key maps will be emitted as how it is input. In other words, it can prevent your keyboard broken when you config is not complete, when unknown keymaps received by kmonad, they won't be handled by kmoand. I recommend you set it to `true` to avoid accident breaking your keyboard.

When `allow-cmd` is true, you can map key to shell command. For example:
```lisp
bi (cmd-button "brightnessctl set +2% >> /dev/null") ;; increase brightness
```
It map the alias bi to run the command `brightnessctl set +2% >> /dev/null`.

### alias
You can alias in kmonad config to avoid repetitive line occur everywhere. To define alias, you need to use the function `defalias`:
```lisp
(defalias

  bi (cmd-button "brightnessctl set +2% >> /dev/null") ;; increase brightness
  bd (cmd-button "brightnessctl set 2%- >> /dev/null") ;; decrease brightness

  bd (cmd-button "brightnessctl set 2%- >> /dev/null" @bi) ;; decrease brightness

  kp1 M-1
  
  kp4 #(s o s o k i n p u i S-2 g m a i l . c o m :delay 25)
)
```
The alias can use in other alias by adding prefix `@`. With prefix `@`, it will automatically expande as the alias recorded.

The parameter of `defalias` be like:
```lisp
(defalias
  <alias> <object to be aliased>
  ...
  ...
)
```
The object can be either **keycode**, **function** or **macros**. Macros, will emit the keycode sequence when it is ran. you can create macros with `#()`. Then alias it a short name for further usage.

## tap-modifier and layer
tap-modifier means that a key can have two prupose when it is tapped and held. An example is `meta`(window key), when you tap it, on Windows OS, applicaton menu will be opened, and you know you can hold it with other keys and somethins will happen. Since most of the keyboard don't leverge tap-modifier, many keys on keyboard can extend its function by convert them into tap-modifier. For example, `alt`, `space`, `shift`, `return` or `ctrl`, they can be more useful! If they have double purpose.

Layer means that your keyboard layout will be vary in different layer. The one you use all day are `shift-layer`, when you hold `shift` the layout of your keyboard change from lower case to upper case.

```lisp
(defalias
  PH (layer-toggle parenthesis)

  EP (tap-next-press = @PH)
)
```
The first line use the function `layer-toggle`.
> The `layer-toggle` button. This button adds a layer to the top of KMonad's layer stack when pressed, and removes it again when released

In simple words, it is same as modifier like `shift` and `ctrl`.

The first line first alias the layer **parenthesis** to **PH**

The second line define the alias **EP** equals to `=` when it is tapped, `@PH` when it is held. `tap-next-press` is a kmonad function determine how keycode is being sent when the buttons is tapped and held.

## talk kmonad how your keyboard look like.
before mappings you have to talk kmonad how you keyboard look like, so that it will handle mappings correctly.
```lisp
;; this my 100% keyboard
(defsrc
  esc  f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12  pause del  home end  pgup  pgdn 
  grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc       nlck kp/  kp*  kp-
  tab  q    w    e    r    t    y    u    i    o    p    [    ]    \          kp7  kp8  kp9  kp+
  caps a    s    d    f    g    h    j    k    l    ;    '    ret             kp4  kp5  kp6
  lsft z    x    c    v    b    n    m    ,    .    /    rsft up              kp1  kp2  kp3  kprt
  lctl lmet lalt           spc            ralt cmp   rctl left down rght      kp0  kp.           
)
```
The format can be ignore, you can write them in single line, to format like this are merely for readability.

{{< details "my keyboard" >}}
![./img/my-keyboard.jpg](img/my-keyboard.jpg)
{{< /details >}}

If you don't know your keyboard layout, you can find it [here](https://github.com/kmonad/kmonad/tree/master/keymap/template) if kmonad have provide yours. Here are some tips, if your keyboard have number pad, you can follow mine version above 
```
nlck kp/  kp*  kp-
kp7  kp8  kp9  kp+
kp4  kp5  kp6
kp1  kp2  kp3  kprt
kp0  kp.           
```
On laptop, `fn`=`fn` unless you are thinkpad user. For thinkpad user `fn`=`wkup`. `print screen`=`sys`.

On external keyboard, `fn`=`cmp`, `print screen`=`pause`.

If kmoand don't provide your keyboard layout, you can try input them line by line.

## default layer
```lisp
(deflayer base
  esc f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12  pause del  home end  pgup  pgdn 
  grv   1    2    3    4    5    6    7    8    9    0    -    =  bspc       nlck kp/  kp*  kp-
  tab   q    w    e    r    t    y    u    i    o    p    [    ]  \          kp7  kp8  kp9  kp+
  @EP   a    s    d    f    g    h    j    k    l    ;    '    ret           kp4  kp5  kp6
  lsft  z    x    c    v    b    n    m    ,    .    /    rsft up            kp1  kp2  kp3  kprt
  lctl  lmet lalt           spc           ralt cmp   rctl left down rght     kp0  kp.
)
```
This layer define how your keyboard normally be without pressing any button. Here I map `@EP` to `caps lock` when you tap the physical `caps lock`, it will insert `=`, when you hold `caps lock` layer **parenthesis** will be active.

If you want to map keys in layer **parenthesis**, you have to
```lisp
(deflayer parenthesis
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _  _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _
  _   _   _   _   @rn   _   _   ]   [   A-o   _   _   _   _     _  _  _  _
  @EP _   _   _   A-f   _   @```   }   {   _   @@: @-> A-ret         _  _  _
  _   _   A-x   _   _   _   _   A-m   A-p  A-n   _   _ _           _  _  _  _
  _   _ _           _         _   _   _   _   _ _           _  _
)
```
You can define the alias and use them by adding prefix `@`, or simply use `A-x` as `alt-x`.

The modifier short name are
```text
`meta-a`  -> `M-a`
`alt-a`   -> `A-a`
`shift-a` -> `S-a`
`ctrl-a`  -> `C-a`
```
Those `-` will fallback to base if you don't specify there purpose. Normally, we only define the keys in layer we use leaving other as `-`

{{< details "tips to create layer with vim" >}}
Select the region in defsrc and use this command `:s/\S\+/-/g`
![./img/changeto-.gif](img/changeto-.gif)
{{< /details >}}

{{< details "my full kmonad config" >}}
If you want to know more about what my keys do, you can mail me.
```
(defcfg
  input  (device-file "/dev/input/by-path/pci-0000:00:14.0-usb-0:4:1.0-event-kbd")
  output (uinput-sink "100 keyboard")
  fallthrough true
  allow-cmd true
)

(defsrc
  esc  f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12  pause del  home end  pgup  pgdn 
  grv  1    2    3    4    5    6    7    8    9    0    -    =    bspc       nlck kp/  kp*  kp-
  tab  q    w    e    r    t    y    u    i    o    p    [    ]    \          kp7  kp8  kp9  kp+
  caps a    s    d    f    g    h    j    k    l    ;    '    ret             kp4  kp5  kp6
  lsft z    x    c    v    b    n    m    ,    .    /    rsft up              kp1  kp2  kp3  kprt
  lctl lmet lalt           spc            ralt cmp   rctl left down rght       kp0  kp.
)

(defalias

  bi (cmd-button "brightnessctl set +2% >> /dev/null") ;; increase brightness
  bd (cmd-button "brightnessctl set 2%- >> /dev/null") ;; decrease brightness

  SS (layer-toggle space-shift)
  LC (layer-toggle control)
  PH (layer-toggle parenthesis)
  lmet (layer-toggle windows)

  ;; layer
  EP (tap-next-press =   @PH)
  SPC (tap-next-press spc @SS)
  ESC (tap-next-press esc @LC)

  ;; Marco
  -> #(- > :delay 20)
  @: #(@ :) ;; vim last command
  , #(C-spc , C-w)

  ``` #(` ` ` :delay 15)

  ;; tmux
  rn #(C-spc , C-w ) ;; rename window
  nw #(C-spc | C-spc !) ;; open new window with the same directory

  ;; resize windows, gtile shortcut
  kp1 M-1
  kp2 M-2
  kp3 M-3

  kp+ M-up
  kprt M-down
  kp* M-left
  kp- M-right

  kp0 C-A-left
  kp. C-A-right
  
  kp4 #(s o s o k i n p u i S-2 g m a i l . c o m :delay 25)
  kp5 #(1 1 5 5 1 9 3 5 0 6 S-2 l i n k . c u h k . e d u . h k :delay 25)
  kp6 #(5 5 3 2 9 4 7 0 :delay 25)

  kp7 #(C-c C-t C-v ret :delay 25) ;; copy and search and new page in browser
  kp8 #(C-t C-v ret :delay 25) ;; search the last copied content in browser new page
  kp9 #(C-c C-f C-v ret :delay 25) ;; select all and copy

  switch A-esc
  ;; hyper
  ALT (tap-next-press lmet ralt)
)

(deflayer base
  caps f1   f2   f3   f4   f5   f6   f7   f8   f9   f10  f11  f12  pause del  home end  pgup  pgdn 
  S-grv 1    2    3    4    5    6    7    8    9    0   \\    `  bspc       nlck kp/  @kp*  @kp-
  tab   q    w    e    r    t    y    u    i    o    p    S-'  [  ]          @kp7  @kp8  @kp9  @kp+
  @EP   a    s    d    f    g    h    j    k    l    ;    -    ret           @kp4  @kp5  @kp6
  @ESC  z    x    c    v    b    n    m    ,    .    /    rsft up            @kp1  @kp2  @kp3  @kprt
  lctl  lmet lalt           @SPC           @ALT cmp   rctl left down rght    @kp0  @kp.
)

(deflayer space-shift
  S-caps S-f1   S-f2   S-f3   S-f4   S-f5   S-f6   S-f7   S-f8   @bd   S-f10  @bi  S-f12  S-pause S-del  S-home S-end  S-pgup  S-pgdn 
  grv S-1    S-2    S-3    S-4    S-5    S-6    S-7    S-8    S-9    S-0   S-\    @```  C-bspc       nlck kp/  kp*  kp-
  S-tab   S-q    S-w    S-e    S-r    S-t    S-y    S-u    S-i    S-o    S-p    '  S-[  S-]            kp7  kp8  kp9  kp+
  S-=  S-a    S-s    S-d    S-f    S-g    S-h    S-j    S-k    S-l    :    S--   S-ret                 kp4  kp5  kp6
  grv  S-z    S-x    S-c    S-v    S-b    S-n    S-m    S-,    S-.    S-/    rsft S-up                 kp1  kp2  kp3  kprt
  lctl  lmet lalt           @SPC           ralt  cmp   rctl S-left S-down S-rght                        kp0  kp.

)

(deflayer control
  C-caps C-f1   C-f2   C-f3   C-f4   C-f5   C-f6   C-f7   C-f8   C-f9   C-f10  C-f11  C-f12  C-pause C-del  C-home C-end  C-pgup  C-pgdn 
  C-grv C-1    C-2    C-3    C-4    C-5    C-6    C-7    C-8    C-9    C-0   C-\    @```  C-bspc       nlck kp/  kp*  kp-
  C-tab   C-q    C-w    C-e    C-r    C-t    C-y    C-u    C-i    C-o    C-p    '  C-[  C-]            kp7  kp8  kp9  kp+
  C-=  C-a    C-s    C-d    C-f    C-g    C-h    C-j    C-k    C-l    :    C--   C-ret                 kp4  kp5  kp6
  @ESC  C-z    C-x    C-c    C-v    C-b    C-n    C-m    C-,    C-.    C-/    rsft C-up                 kp1  kp2  kp3  kprt
  lctl  lmet lalt           C-spc           ralt  cmp   rctl C-left C-down C-rght                        kp0  kp.

)

(deflayer parenthesis
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _  _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _
  _   _   _   _   @rn   _   _   ]   [   A-o   _   _   _   _     _  _  _  _
  @EP _   _   _   A-f   _   @```   }   {   _   @@: @-> A-ret         _  _  _
  _   _   A-x   _   _   _   _   A-m   A-p  A-n   _   _ _           _  _  _  _
  _   _ _           _         _   _   _   _   _ _           _  _
)

(deflayer windows
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _  _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _
  _ _   _   _   _   _   _   _   _   _   _ _ _         _  _  _
  @switch   _   _   _   _   _   _   _   _  _   _   _ _           _  _  _  _
  _   _ _           _         _   _   _   _   _ _           _  _
)

#|                                                               
(deflayer name-of-the-layer
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _ _  _  _ 
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _ _  _  _
  _   _   _   _   _   _   _   _   _   _   _   _   _   _     _  _  _  _
  _   _   _   _   _   _   _   _   _   _   _   _   _         _  _  _
  _   _   _   _   _   _   _   _   _   _   _   _ _           _  _  _  _
  _   _ _           _         _   _   _   _   _ _           _  _
)
|#
```
{{< /details >}}

{{< details "run kmonad at startup with systemd" >}}
create `/usr/lib/systemd/system/kmonad.service`
```
sudo -e /usr/lib/systemd/system/kmonad.service
```
add those line into `/usr/lib/systemd/system/kmonad.service`

```service
[Unit]
Description=kmonad keyboard config

[Service]
Restart=always
RestartSec=3
ExecStart=/path/to/kmonad /path/to/config.kbd
Nice=-20

[Install]
WantedBy=default.target
```
Find kmonad by 
```sh
which kmonad
```
Enable the service
```sh
sudo systemctl daemon-reload
sudo systemctl start kmonad.service
sudo systemctl enable kmonad.service
```
{{< /details >}}

