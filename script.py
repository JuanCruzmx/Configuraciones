import os
import platform
import shutil

def config_vim():
    sistema = platform.system()         # Detección del sistema
    home = os.path.expanduser("~")      # Busca carpeta de usuario
    
    if sistema == "Windows":
        nombre_archivo = "_vimrc"
    else:
        nombre_archivo = ".vimrc"
    
    ruta = os.path.join(home, nombre_archivo)
    latex = shutil.which("pdflatex") is not None   

    config = [
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
        '"  --- Comandos ---',
        'nnoremap <C-z> :w<CR>:!pdflatex %<CR>',
    ]
    
    with open(ruta, 'w') as f:
        f.write("\n".join(config))
    
    print(f'¡Vim configurado en {sistema}!')
    print(f'Ruta: {ruta}')

if __name__ == '__main__':
    config_vim()
