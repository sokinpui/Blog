---
title: "DIY split keyboard with ergogen"
date: 2023-09-07T08:48:57+08:00
tags: [""]
author: "So Kin Pui"
showToc: true
TocOpen: true
draft: false
hidemeta: false
comments: true
description: "Design simple split keyboard with PCB board"
canonicalURL: ""
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

type of DIY keyboard
  hand wiring keyboard or PCB board


draw keyboard layout using ergogen
PCB trace routing
PCB manufractor
Soldering tips
flash boot loader
  recommend use Mac and Windows, as a GUI tool is avalible for auto-flash.

is DIY keyboard better than sold keyboard?
  To me, probably not, Since I prefer more key than less key profile, so that I can define more macro keys. I can accept tap a key far away rather than holding many keys at the same time.
  I find typing on staggered keyboard is lot more natural on ortholinear, the power of muscle memory.
  The \$200 keyboard is the most comfortable keyboard I have use. No matter the profile, numbers of key, layout. incline degree


DIY keyboard maybe easier than you think. After decide the number of keys will on your keyboard, you can design the layout how the keyboard look like, then soldering the necessary part, flash the bootloader of the micro-controller on your keyboard, everyhing is done!

# Method to build a keyboard
1. Use PCB
2. Hand wiring

<!--
image here
-->

Keyboard with PCB will usually give you flat profile, like putting keycaps on a flat board( actually it is ). The PCB itself is firm enough, I have seen quite a lot keyboard use PCB don't equip with case. PCB will be elegant choice for minimalized keyboard design.
<!--
image
-->

On the other hands, hand wiring has more flexibility, it can easily fit different shape of the keyboard case, like [dactyl keyboard](https://github.com/adereth/dactyl-keyboard), in such case, handwiring maybe allow you have easier soldering and fit different rows with their own degree. Moreover, PCB is usually expensive than hand-wiring. Nevertheless, you may find PCB a lot easier as the starting point of keyboard DIY journal.

One of the advantages of PCB is that you can find many well routed PCB which are ready to use. You don't even have to design your keyboard layout when you are DIY! WAIT, WHAT?

I would pick PCB since it is a lot easier, even when I face difficult, I can simply give up and use some of the PCB that is open-source. I still able to enjoy the is open-source.. I still able to enjoy the soldering time..
