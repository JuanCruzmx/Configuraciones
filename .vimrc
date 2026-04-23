" --- Personalización Visual ---
syntax on
colorscheme desert
set number
set relativenumber
set cursorline

" --- Comportamiento ---
set clipboard=unnamedplus
set mouse=a
set tabstop=4
set shiftwidth=4
set expandtab

" --- Atajos de compilación ---
nnoremap <F5> :w<CR>:!pdflatex %<CR>