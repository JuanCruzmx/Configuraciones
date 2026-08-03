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
function! Latex()
    w
    execute '!pdflatex -interaction=nonstopmode ' . shellescape(expand('%'))
   
    if has('mac')
        silent execute '!rm -f ' . shellescape(expand('%:r') . '.log') . ' ' . shellescape(expand('%:r') . '.aux') . ' ' . shellescape(expand('%:r') . '.out')
        silent execute '!open ' . shellescape(expand('%:r') . '.pdf')
    else
        if has('win32') || has('win64')
            silent execute '!del ' . shellescape(expand('%:r') . '.log') . ' ' . shellescape(expand('%:r') . '.aux') . ' ' . shellescape(expand('%:r') . '.out')
        else
            silent execute '!rm -f ' . shellescape(expand('%:r') . '.log') . ' ' . shellescape(expand('%:r') . '.aux') . ' ' . shellescape(expand('%:r') . '.out')
        endif
        silent execute '!powershell.exe -c start ' . shellescape(expand('%:r') . '.pdf')
    endif
    
    redraw!
endfunction

autocmd BufRead,BufNewFile *.tex nnoremap <buffer> <C-b> :call Latex()<CR>
