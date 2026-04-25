import os
import platform
import shutil

def config_vim():
    sistema = platform.system()         # Detección del sistema
    home = os.path.expanduser("~")      # Busca carpeta de usuario
    
    if sistema == 'Windows':
        nombre_vim = '_vimrc'
        abrir_pdf = '!start chrome "%:r.pdf"'
    elif sistema == 'Darwin':
        nombre_vim = '.vimrc'
        abrir_pdf = '!open -a "Google Chrome" "%:r.pdf"'
    else:
        nombre_vim = ".vimrc"
        abrir_pdf = '!explorer.exe "%:r.pdf"'
    
    ruta = os.path.join(home, nombre_vim)
    latex = shutil.which("pdflatex") is not None   

    plantilla_latex = [
        r'\documentclass{article}',
        r'\usepackage[utf8]{inputenc}',
        r'\usepackage[spanish]{babel}',
        r'\usepackage{amsmath, amssymb}',
        r'',
        r'\title{}',
        r'\date{\today}',
        r'\author{Juan Cruz Osorio}',
        r'',
        r'\begin{document}',
        r'',
        r'\end{document}',
    ]

    vim = [
        '"  --- Configuraciones básicas ---',
        'syntax on',
        'set number',
        'set relativenumber',
        'set mouse=a',
	    'set tabstop=4',
	    'set shiftwidth=4',
	    'set expandtab',
        'set cursorline',
        'set laststatus=2',
        'set showmode',
        'set showmatch',
        'set clipboard=unnamedplus',
        '"  --- Estilos ---',
        'set background=dark',
	    'colorscheme desert',
        '"  --- Comandos y funciones ---',
        f'autocmd BufEnter *.tex nnoremap <buffer> <C-b> :w<CR>:!pdflatex % && rm -f "%:r.aux" "%:r.log" "%:r.out"<CR>:{abrir_pdf}<CR><CR>',
        'function! PlantillaLatex()',
        *[f"    call setline({i+1}, '{linea.replace(chr(39),chr(39)+chr(39))}')" for i, linea in enumerate(plantilla_latex)],
        '   execute "normal! 11G" | startinsert',
        'endfunction',
        'autocmd BufNewFile *.tex call PlantillaLatex()',
    ]
    
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write("\n".join(vim))
    
    print(f'¡Vim configurado en {sistema}!')
    print(f'Ruta: {ruta}')

if __name__ == '__main__':
    config_vim()
