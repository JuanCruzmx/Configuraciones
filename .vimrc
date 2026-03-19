if has("win32") || has("win64")
	set directory=$HOME/AppData/Local/Temp//
	let g:ruta_git = expand('<sfile>:p:h')
else
	set directory=/tmp//
	let g:ruta_git = expand('<sfile>:p:h')
endif

function! CopilarLatex()
	if has("win32") || has("win64")
		let l:separador = ';'
		let l:borrar = 'del *.aux *.log *.out *.toc *.fdb_latexmk *.fls'
		let l:abrir = 'start'
	else
		let l:separador = ':'
		let l:borrar = 'rm -f *.aux *.log *.out *.toc *.fdb_latexmk *.fls'
		let l:abrir = 'xdg-open'
	endif
	
	let l:ruta_estilos = g:ruta_git . '/Config-Latex//'
	let $TEXINPUTS = '.' . l:separador . l:ruta_estilos . l:separador
	
	execute "!pdflatex % && pdflatex % && " . l:borrar . " && " . l:abrir . " %:r.pdf"
endfunction

syntax on
set number
set relativenumber

set tabstop=4
set shiftwidth=4
set softtabstop=4

set clipboard=unnamed

autocmd FileType tex nnoremap <C-c> :w<CR>:call CopilarLatex()<CR>
