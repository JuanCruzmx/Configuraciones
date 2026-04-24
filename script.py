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
        'set mouse=a',
	    'set tabstop=4',
	    'set shiftwidth=4',
	    'set expandtab',
	    'colorscheme desert',
    ]

    if latex:
        config.append('nnoremap <C-c> :w<CR>:!pdflatex %<CR>')
        mensaje = 'LaTeX detectado...'
    else:
        mensaje = 'No se encontro LaTeX...'
    
    with open(ruta, 'w') as f:
        f.write("\n".join(config))
    
    print(f'¡Vim configurado en {sistema}!')
    print(f'Ruta: {ruta}')
    print(mensaje)

if __name__ == '__main__':
    config_vim()
