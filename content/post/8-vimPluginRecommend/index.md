---
title: "Vim plugin recommendation"
#description: <descriptive text here>
date: 2023-06-29T14:00:02+08:00
draft: false
toc: true
image: ""
tags: []
categories: []
---

Vacillate vim are really good, after remember some vim command keyblindings, you can start editing or writing immediately. The main benefits of using plugins can avoid use our poor vimscript. Use some great plugin avoid you to rebuild the wheel. Before you are able to write plugin yourself, trust me, any exist plugins is better than yours. 

# Plugins recommendation
## 1. [vim-plug](https://github.com/junegunn/vim-plug)
vim-plug, a plugin manager that help you install, update and **manage** your plugins. Vim come with built-in package manger `pack`, a subdirectory under `.vim/`, if don't exist, create it. I usually use build-in `pack` only for some personal little script, so that I don't have to move forth and back in vim runtime path. 

Vim plug syntax is easy, to add random plugins, add those line in your `.vimrc`:
```
call plug#begin()
" list plugins herer
Plug 'junegunn/vim-easy-align'
call plug#end()
```
Any github repo can be installed, for example, you have write your *plugin* and push to github at https://github.com/username/plugin-name, you can add this *plugin* by adding those line in your `.vimrc`:
```
call plug#begin()
" list plugins herer
Plug 'username/plugin-name'
call plug#end()
```
After that, save your file by `:w`, source your `.vimrc` or leave then reopen your `.vimrc`, run the command `:PlugInstall`. Plugins will be installed at `~/.vim/plugged` by default.

To save my little pinky finger, I have those mapping for convenience:
```
nnoremap \i :w<cr>:source ~/.vim/vimrc<cr>:PlugInstall<cr>
nnoremap \c :w<cr>:source ~/.vim/vimrc<cr>:PlugClean<cr>
nnoremap \u :w<cr>:source ~/.vim/vimrc<cr>:PlugUpdate<cr>
```

## 2. [vim-sandwich](https://github.com/machakann/vim-sandwich)
vim-sandwich help you to change the surround of text. What is surround? Surround means the pairs that surround text object, like `"` and `(`. It is handy to let program do for us, instead of change manually.

[vim-sandwich](https://github.com/machakann/vim-sandwich) is an alternative of [vim-surround](https://github.com/tpope/vim-surround), which provide texthighligh, auto-selection, and repeat with `.` out-of the box. It use less keys than vim-surround, just navigate to the current parenthesis object position and chagne the surround! No need to select the object before change.
surround style of changing surround:
```
cs <surround to be changed> <surround to replace>
```

sandwich style of changing surround(auto replace):
```
srb <surround to be changed> <surround to replace>
```
I though it is a more intutitive than to surround style of change, as symbol like `{`, `[` and `(` is more difficult to type than navigate to the right position with `f`, `t`, `F` and `T`.

The auto-selection of vim-sandwich is highlight of this plugin, I have use this feaatur for all surround editing including add, delete and replace surrounds. I have the following setting so that I can use `<leader>+symbols` to add surround for one words or selected region 
```
nmap <leader>( saiw(E
nmap <leader>) saiw)E
nmap <leader>[ saiw[E
nmap <leader>] saiw]E
nmap <leader>{ saiw{E
nmap <leader>} saiw}E
nmap <leader>" saiw"E
nmap <leader>' saiw'E
nmap <leader>< saiw<E
nmap <leader>> saiw>E
nmap <leader>` saiw`E
nmap <leader>$ saiw$E
nmap <leader>* saiw*.E
nmap <leader>~ saiw~.E

" visual
vmap <leader>( sa(
vmap <leader>) sa)
vmap <leader>[ sa[
vmap <leader>] sa]
vmap <leader>{ sa{
vmap <leader>} sa}
vmap <leader>" sa"
vmap <leader>' sa'
vmap <leader>< sa<
vmap <leader>> sa>
vmap <leader>` sa`
vmap <leader>$ sa$
vmap <leader>_ ca_
vmap <leader>* sa*.
vmap <leader>~ sa~.
```
However, it is a bad habits to make a keyboard macros, the better way would be calling the plugin's function. Coz I am lazy and nothing happen till now, I keep those lines.
<!--
add git to show
-->

## 3. [clever-f](https://github.com/rhysd/clever-f.vim) 
[clever-f](https://github.com/rhysd/clever-f.vim) is a plugin that improve the smoothness and consisent when navigation with `f`, `t`, `F` and `T`. You can use `f` to navigate to next `f` search, or use `F` to navigate backwards, instead of using `;` and `,`. What's more, you can remap `;` and `,` for other purpose. When you press `f` to navigate `f` search, you can cross the line, and you can have smart case searching! 

After using this plugin, I won't claim it is more efficient than `;` and `,`, but it must be more comfortable.

You can change the behaviour of the plugins by adding those line to your `.vimrc`.
```
" ignore case unless you specify Upper case 
let g:clever_f_smart_case = 1  

" allow cross line, set to 1 if you don't 
let g:clever_f_across_no_line = 0 like it

" f; will searhc for all symbols
let g:clever_f_chars_match_any_signs = ';' 

" f. will repeat you last search
let g:clever_f_repeat_last_char_inputs = [ "\<TAB>" ]
```

<!--
TODO add a gif to show f; and f t T F
-->

## 4. [coc.nvim](https://github.com/neoclide/coc.nvim)
[coc.nvim](https://github.com/neoclide/coc.nvim) make completion in vim like vscode.

coc.nvim is a plugins framework, so you may find coc-XXX plugin written in Javascript or Typescript. Some of them is unique, some of them is alternative to the existing vim plugins to compatilbe with coc.nvim. One is [coc.snippets](https://github.com/neoclide/coc-snippets), which aims to replace [Ultisnips](https://github.com/SirVer/ultisnips) when you use coc.nvim. coc.nvim use is written Javascript and Typescript, you will configure the popup window in JSON file.

By default, coc.nvim don't come with any keyblindings, you have to configure yourself.

For example, you can:

```
"   coc.nvim
inoremap <silent><expr> <TAB> coc#pum#visible() ? coc#pum#next(1) : 
      \ cocfunc#CheckBackspace() ? "\<TAB>" : coc#refresh()

inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<S-TAB>"

inoremap <silent><expr> <CR> coc#pum#visible() ? "\<C-g>u\<CR>\<c-r>=coc#pum#close()\<CR>" 
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

inoremap <silent><expr> <space> coc#pum#visible() ? "<esc>a<space>" 
                              \: "<space>"

"   coc.snippets
inoremap <C-j> <Plug>(coc-snippets-expand-jump)
vnoremap <C-j> <Plug>(coc-snippets-select)
let g:coc_snippet_next = '<C-j>'
let g:coc_snippet_prev = '<C-k>'
```

The above example don't require selection, you use `<TAB>` and `<S-TAB>` to navigate to the suggestion you want, after that, you can press `<space>` and `<cr>` to move and start a new line respectively.

## 5. [fzf.vim](https://github.com/junegunn/fzf.vim)
[fzf.vim](https://github.com/junegunn/fzf.vim) $\times$  vim, a command line tools [fzf](https://github.com/junegunn/fzf) vim warpper. You can unlock the power of fuzzy finder in vim nearly anything.

The syntax of fzf.vim is simple:<br>
:Files [PATH] 	search file in current directory by default <br>
:Buffers 	search opened buffers <br>
:Ag [PATTERN] 	use ag to search pattern <br>
:Rg [PATTERN] 	use rg to search pattern <br>
:Lines [QUERY] 	search lines in loaded buffers <br>
:Marks 	search marks and jump to <br>
:History 	serach for opened files <br> 
:History: 	search fo Command history <br> 
:History/ 	Search for searching history wiht `/` <br> 
:Commands 	search for avalible Commands <br> 
:Maps 	serahc for Normal mode mappings <br> 
:Helptags 	fzf for :help XXX, open help buffer <br> 

you can make your own shortcut like
```
let g:fzf_preview_window = ['right,50%', 'ctrl-/']
let g:fzf_layout = {'window': { 'width': 0.9, 'height': 0.9 }}
let g:fzf_buffers_jump = 1

nnoremap <leader>ff :Files<cr>
nnoremap <leader>fb :Buffers<cr>
nnoremap <leader>fs :Lines<cr>
nnoremap <leader>fp :Rg<cr>
nnoremap <leader>f/ :History/<cr>
nnoremap <leader>f: :History:<cr>
nnoremap <leader>fh :Helptags<cr>
```
The first line config the location of preview windows, you can have `right`, `left`, `up`, and `down`. The second line control the size of the popup windows

<!--
TODO intro bat also to config the color scheme.
-->
