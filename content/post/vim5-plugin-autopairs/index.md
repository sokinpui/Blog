---
title: "Neovim plugins recommendation: Auto pair and multi cursor"
date: 2023-08-03T22:23:12+08:00
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
description: "Auto pair plugin that work with multi cursor without any issue."
canonicalURL: "https://canonical.url/to/page"
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

I use multi cursor plugin and auto pairs together, unfortunately I find my old two plugins don't integrate well. [This autopairs from LunarWatcher](https://github.com/LunarWatcher/auto-pairs) often throw error: `E117: Unknown function: AutoPairsTryInit` when end editing with [multi cursor plugin]((https://github.com/mg979/vim-visual-multi). Although this plugin is already improved to be more compatible with **vim-visual-multi**. To be mentioned, this bug is fixed in this [issue](https://github.com/LunarWatcher/auto-pairs/issues/12#issue-780680284). I still find the bug occur.

# Another auto pair plugins
I google a solution, and finally end up with this Neovim plugins [nvim-autopairs](https://github.com/windwp/nvim-autopairs). Surprisingly, it is feature richer than [this autopairs plugins](https://github.com/LunarWatcher/auto-pairs), unfortunately, it only support Neovim.

Other than basic function, you can extend its auto pairs rule by calling its rule method: (example from its repo)
```lua
local Rule = require('nvim-autopairs.rule')
npairs.add_rules({
  Rule("$", "$",{"tex", "latex"})
    -- don't add a pair if the next character is %
    :with_pair(cond.not_after_regex("%%"))
    -- don't add a pair if  the previous character is xxx
    :with_pair(cond.not_before_regex("xxx", 3))
    -- don't move right when repeat character
    :with_move(cond.none())
    -- don't delete if the next character is xx
    :with_del(cond.not_after_regex("xx"))
    -- disable adding a newline when you press <cr>
    :with_cr(cond.none())
  },
  -- disable for .vim files, but it work for another filetypes
  Rule("a","a","-vim")
)
```

Their already have some common rule that provided by its [wiki](https://github.com/windwp/nvim-autopairs/wiki/Custom-rules). One of the very helpful rule is auto addspace on =.
```
var| 
insert =
var = |
insert = again
var == |
```

Also the plugin provide api for you to disable it per filetype. If you writing shell script you don't auto addspace on =, you can diable it by:
```lua
local Rule = require('nvim-autopairs.rule')
npairs.add_rules({
      Rule("=", "", "-sh")
          --rule body
})

```

You can write your own rule to fullfill your need. Most importantly, it won't throw error if use with **vim-visual-multi**!
