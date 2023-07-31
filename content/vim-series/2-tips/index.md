---
title: "Simple hacking and tips to reduce pain in Vim"
date: 2023-07-23T10:18:20+08:00
draft: true
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
description: "Simple vimscript that enhance user experience"
canonicalURL: "https://canonical.url/to/page"
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true

---

Aims to less pain when using vim, if you find other plugins perform the same functionality, I would say use that plugin instead, because plugins usually provide broader function and easier for management compare to discrete vimscript.

# Highlight in search
Want Highlight when searching? Dirty but workable solution can map search key into:
```
nnoremap / :set hlsearch<cr>/
nnoremap ? :set hlsearch<cr>?

nnoremap n :set hlsearch<cr>n
nnoremap N :set hlsearch<cr>N

nnoremap * :set hlsearch<cr>*
nnoremap # :set hlsearch<cr>#

vnoremap * *:set hlsearch<cr>
vnoremap # #:set hlsearch<cr>
```

Delete highlight after search:
```
autocmd insertenter * set nohlsearch
autocmd textchanged * set nohlsearch
```
Clear highlight when enter insert mode, clear highlight when any text being edited.

# Hide Cursorline in inactive window
Do you find inactive window still have cursorline shown? Hack with following code:
```
augroup CursorLine
    autocmd!
    autocmd VimEnter * setlocal cursorline
    autocmd WinEnter * setlocal cursorline
    autocmd BufWinEnter * setlocal cursorline
    autocmd WinLeave * setlocal nocursorline
augroup END
```

# Open help page in split window
```
augroup Init_buffer
    autocmd!
    autocmd BufEnter *.txt if &buftype == 'help' | if winnr('$') <= 2 | wincmd H | endif | endif  
augroup END
```
Since I seldom use vim split window in vim, if I really need to split window, I will first use tmux split window. When I need Vim manual, I also want to know what is happening on my current buffer.

# Cursor back to last position
```
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
```

# find digital
```
nnoremap <Leader>n /\d\+<cr>
```
A simple Vim regular expression hacking.

# Paste in visual mode without pollute register
Since paste in visual mode will first delete content, if you don't want to pollute your register and keep `p` the same content, following code may help you.
```
xnoremap <leader>p "_dP
```

# Number of search items in status line
give more information when searching, you can know numbers of item you search, and the location. This simple hacking is provided by Vim manual, see `:help searchcount`.
```
function! s:update_searchcount(timer) abort
    if a:timer ==# s:searchcount_timer
        call searchcount(#{
                    \ recompute: 1, maxcount: 0, timeout: 100})
        redrawstatus
    endif
endfunction

function! statusline#LastSearchCount() abort
    let result = searchcount(#{recompute: 1})
    if empty(result)
        return ''
    endif
    if result.incomplete ==# 1     " timed out
        return printf(' [%s] [?/??]', @/)
    elseif result.incomplete ==# 2 " max count exceeded
        if result.total > result.maxcount &&
                    \  result.current > result.maxcount
            return printf(' [%s] [>%d/>%d]', @/,
                        \             result.current, result.total)
        elseif result.total > result.maxcount
            return printf(' [%s] [%d/>%d]', @/,
                        \             result.current, result.total)
        endif
    endif
    return printf(' [%s] [%d/%d]', @/,
                \             result.current, result.total)
endfunction

let &statusline ..= '%=%-5.{statusline#LastSearchCount()} %(%l,%c-%v%) %p%%'

autocmd CursorMoved,CursorMovedI *
            \ let s:searchcount_timer = timer_start(
            \   200, function('s:update_searchcount'))
```
