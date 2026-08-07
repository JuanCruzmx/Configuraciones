filetype plugin indent on
syntax on
set number
set relativenumber
set cursorline
set mouse=a

set expandtab
set tabstop=4
set shiftwidth=4
set clipboard=unnamedplus
set autoindent
set smartindent
set noswapfile
set nobackup

"   Estilos
set t_Co=256
set background=dark

"   Plantillas
let mapleader = ' '
autocmd BufNewFile *.tex 0r ~/.vim/Plantillas/plantilla.tex
autocmd BufNewFile *.md 0r ~/.vim/Plantillas/plantilla.md
autocmd BufNewFile *.html 0r ~/.vim/Plantillas/plantilla.html

"   Comandos
autocmd BufRead,BufNewFile *.tex nnoremap <buffer> <C-b> :w<CR>:silent !pdflatex -interaction=nonstopmode '%' && rm -f '%:r.log' '%:r.aux' '%:r.out' '%:r.pyg' && powershell.exe -c start '%:r.pdf' <CR>:redraw!<CR>
