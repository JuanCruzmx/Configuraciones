syntax on
set number
set relativenumber

set tabstop=4
set shiftwidth=4
set softtabstop=4

set clipboard=unnamed
set directory=$HOME/AppData/Local/Temp//

autocmd FileType tex nnoremap <C-c> :w<CR>:let $TEXINPUTS='.;C:/Users/juanc/Desktop/JuanCruz/Git/Configuraciones/Config-Latex//' <Bar> :!pdflatex % && pdflatex % && del *.aux *.log *.out *.toc *.fdb_latexmk *.fls && start %:r.pdf<CR>
