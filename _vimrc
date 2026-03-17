syntax on
set number
set relativenumber

set tabstop=4
set shiftwidth=4
set softtabstop=4

set clipboard=unnamed
set directory=$HOME/AppData/Local/Temp//

autocmd FileType tex nnoremap <C-c> :w<CR>:!taskkill /IM Acrobat.exe /F 2>null & pdflatex % && del *.aux *.log *.out *.toc *.fdb_latexmk *.fls && start %:r.pdf<CR>
