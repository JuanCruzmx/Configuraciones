"  --- Configuraciones básicas ---
syntax on
set number
set relativenumber
set mouse=a
set tabstop=4
set shiftwidth=4
set expandtab
set cursorline
set laststatus=2
set showmode
set showmatch
set clipboard=unnamedplus
"  --- Estilos ---
set background=dark
colorscheme desert
"  --- Comandos ---
nnoremap <C-z> :w<CR>:!pdflatex %<CR>
