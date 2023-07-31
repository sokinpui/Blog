---
title: "Markdown writing, Obsidian + Vim, not vim-mode"
#description: <descriptive text here>
date: 2023-06-30T10:25:46+08:00
draft: false
toc: true
image: ""
tags: []
categories: []
---

[Obsidian](https://obsidian.md/) is a local note-taking apps, all the files are saved as `.md` or `.pdf` format. 
[Vim](https://www.vim.org/) or [Neovim](https://neovim.io/) are great editors that allow you config all days without writing any real code

Obsidian has vim-mode, which support Vim modal editing out of the box. However, due to the font size is not unqiue in obsidian, Like the heading has bigger size, the code block is not at the beginning of the line. Sometimes got confused when using jk to move up and down, you move up may not be where you want to go. Vim modal editing editing works better with mono font, regardly, mono font has less readibility than non-mono font where obsidian used by default. What's more, obsidian vim-mode is not clone of vim, still implement as a vim emulation. You may have [obsidian vimrc support plugin](https://github.com/esm7/obsidian-vimrc-support), so to unlock the power of mapping in obsidian, but you still got a lot limitation. In terms of editing, a real Vim should be better than any vim-emulation, and in terms of notes-taking, any note-taking app should work better than Vim+shell, you don't have notes structure visualization without some extra tweaks.

# Editing in Vim
With Vim, you can have those convenience over obsidian:
1. snippets
2. completion
3. The best "Vim" mode

The last one should have no doubt. The reason I use snippets and completion in note-taking because I am lazy. Retype the same works again and again are really boring and meangless. Obsidian does have some plugins related to [snippets](https://github.com/ArianaKhit/text-snippets-obsidian) and [completion](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin), but setup snippets and completion is just easier and more consisent on Vim. In Vim you can have same UI interface and consisent keyblindings.<br>
The plugins I use for snippets and completion are [coc.nvim](https://github.com/neoclide/coc.nvim) + [Ultisnips](https://github.com/SirVer/ultisnips) + [coc.snippets](https://github.com/neoclide/coc-snippets), choosing coc.nvim simply because it have provided solution for snippets together with completion out of the box. Of course, there is so much alternatives avalible. The only missing is the backlink completion. But it is fine, insert backlink in obsidian let me have a look of filenames, so that I won't forget the filename and suck typing.

Example configuration for snippets and completion:
```
Plug 'neoclide/coc.nvim', {'branch': 'release'}

"   coc.nvim
inoremap <silent><expr> <TAB> coc#pum#visible() 
      \ ? coc#pum#next(1) : 
      \ cocfunc#CheckBackspace() 
      \ ? "\<TAB>" : coc#refresh()

inoremap <expr><S-TAB> coc#pum#visible() 
      \ ? coc#pum#prev(1) : "\<S-TAB>"

inoremap <silent><expr> <CR> coc#pum#visible() 
      \ ? "\<C-g>u\<CR>\<c-r>=coc#pum#close()\<CR>" 
      \ : "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

inoremap <silent><expr> <space> coc#pum#visible() 
      \ ? "<esc>a<space>" : "<space>"


"   coc.snippets
inoremap <C-j> <Plug>(coc-snippets-expand-jump)
vnoremap <C-j> <Plug>(coc-snippets-select)
let g:coc_snippet_next = '<C-j>'
let g:coc_snippet_prev = '<C-k>'
```

coc.snippets need to be installed separately, after install coc.nvim, run the command `:CocInstall coc-snippets`


# Obsidian, the markdown viewer
Insert image in markdown with plugins [image resizer](https://github.com/nicojeske/mousewheel-image-zoom) and [imager inserter](https://github.com/reorx/obsidian-paste-image-rename) is supar convenient, no doubt better than vim.

## Navigation in wrapped line
Since hard wrapped line will make paragraph look ugly in Obsidian, use soft wrapped line instead, which means one paragraph is actually a long long line. Some mapping will be handy to avoid keep using prefix `g` again in Vim.

Example configuration, in `~/.vim/ftplugin/markdown.vim:`

```
setlocal textwidth=0 wrap formatoptions=tc2n linebreak

noremap <buffer> j gj
noremap <buffer> k gk
noremap <buffer> $ g$
noremap <buffer> ^ g^
noremap <buffer> 0 g0

nnoremap <buffer> dd g0vg$D
nnoremap <buffer> D g0vg$D
nnoremap <buffer> V g0vg$

nnoremap <buffer> I g^i

function! IsBlank()
    normal! g$
    var char = getline(".")[col(".") - 1]
    if char == "\t" || char == " "
        normal! gel
        startinsert
    else
        startinsert!
    endif
deffunction 

nnoremap <buffer> A :call IsBlank()<cr>
```
The last one help you stop at the last non-blank character in wrapped line, the normal behavior of `g$a` will stop at the last character including space and tab, sometimes inconvenient. 

## Psudo WYSIWYG
WYSIWYG, what you see is what you get, is one of the highlight of markdown syntax, very simple. To get half experience in Vim, oen can be turn on concealment. `set conceallevel=2` to convert highlight syntax into unicode character.

Just let better tools takes the jobs. For text editing, take Vim; For notes managment, take Obsidian; For complex data representaion like chart, embedded image and website page, just take any other tools like Notion.

<!--
TODO image example
-->
