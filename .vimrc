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
"  --- Comandos y funciones ---
autocmd BufEnter *.tex nnoremap <buffer> <C-b> :w<CR>:!pdflatex % && rm -f "%:r.aux" "%:r.log" "%:r.out"<CR>:!explorer.exe "%:r.pdf"<CR><CR>
function! PlantillaLatex()
    call setline(1, '\documentclass{article}')
    call setline(2, '\usepackage[utf8]{inputenc}')
    call setline(3, '\usepackage[spanish]{babel}')
    call setline(4, '\usepackage{amsmath, amssymb}')
    call setline(5, '')
    call setline(6, '\title{}')
    call setline(7, '\date{\today}')
    call setline(8, '\author{Juan Cruz Osorio}')
    call setline(9, '')
    call setline(10, '\begin{document}')
    call setline(11, '')
    call setline(12, '\end{document}')
   execute "normal! 11G" | startinsert
endfunction
autocmd BufNewFile *.tex call PlantillaLatex()