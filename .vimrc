"  --- Configuraciones ---
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
set termguicolors
colorscheme desert
"  --- Comandos ---
autocmd BufEnter *.tex nnoremap <buffer> <C-b> :w<CR>:!pdflatex % && rm -f "%:r.aux" "%:r.log" "%:r.out"<CR>:!explorer.exe "%:r.pdf"<CR><CR>
"  --- Funciones ---
function! PlantillaLatex()
    call setline(1, '\documentclass{article}')
    call setline(2, '\usepackage[utf8]{inputenc}')
    call setline(3, '\usepackage[spanish]{babel}')
    call setline(4, '\usepackage{amsmath, amssymb}')
    call setline(5, '\usepackage{graphicx}')
    call setline(6, '\usepackage[margin=2.5cm]{geometry}')
    call setline(7, '\usepackage{hyperref}')
    call setline(8, '\setlength{\parindent}{0pt}')
    call setline(9, '')
    call setline(10, '\title{}')
    call setline(11, '\date{\today}')
    call setline(12, '\author{Juan Cruz}')
    call setline(13, '')
    call setline(14, '\begin{document}')
    call setline(15, '')
    call setline(16, '\end{document}')
   execute "normal! 14G" | startinsert
endfunction
autocmd BufNewFile *.tex call PlantillaLatex()