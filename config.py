import os
import platform
import shutil

class Config:
    def __init__(self):
        self.os = platform.system()         # Detección del sistema
        self.home = os.path.expanduser("~")      # Busca carpeta de usuario
        self.herramientas = ['vim', 'git', 'pdflatex', 'python3', 'gcc']    
        self.tema = 'desert'
        self.sistema()
        self.verificar()
    def sistema(self): 
        if self.os == 'Windows':
            self.nombre_vim = '_vimrc'
            self.abrir_pdf = '!start chrome "%:r.pdf"'
        elif self.os == 'Darwin':
            self.nombre_vim = '.vimrc'
            self.abrir_pdf = '!open -a "Google Chrome" "%:r.pdf"'
        else:
            self.nombre_vim = ".vimrc"
            self.abrir_pdf = '!explorer.exe "%:r.pdf"'
    def plantilla_latex(self):
        self.plantilla = [
            r'\documentclass{article}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[spanish]{babel}',
            r'\usepackage{amsmath, amssymb}',
            r'\usepackage{graphicx}',
            r'\usepackage[margin=2.5cm]{geometry}',
            r'\usepackage{hyperref}',
            r'',
            r'\title{}',
            r'\date{\today}',
            r'\author{Juan Cruz}',
            r'',
            r'\begin{document}',
            r'',
            r'\end{document}',
        ]
    def config_vim(self):
        self.vim  = [
            '"  --- Configuraciones ---',
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
            'set termguicolors',
            f'colorscheme {self.tema}',
            '"  --- Comandos ---',
            f'autocmd BufEnter *.tex nnoremap <buffer> <C-b> :w<CR>:!pdflatex % && rm -f "%:r.aux" "%:r.log" "%:r.out"<CR>:{self.abrir_pdf}<CR><CR>',
            '"  --- Funciones ---',
            'function! PlantillaLatex()',
            *[f"    call setline({i+1}, '{linea.replace(chr(39),chr(39)+chr(39))}')" for i, linea in enumerate(self.plantilla)],
            '   execute "normal! 14G" | startinsert',
            'endfunction',
            'autocmd BufNewFile *.tex call PlantillaLatex()',
        ]
    def archivos(self):
        self.plantilla_latex()
        self.config_vim()
        self.ruta = os.path.join(self.home, self.nombre_vim)
        with open(self.ruta, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.vim))
    def verificar(self): 
        self.archivos()
        print(f'Sistema Operativo: {self.os}')
        print(f'{"vimrc".ljust(10)} | {str(os.path.exists(self.ruta)).ljust(10)} | {self.ruta}')
        for h in self.herramientas:
            verificar = shutil.which(h) is not None
            print(f'{h.ljust(10)} | {str(shutil.which(h) is not None).ljust(10)} | {shutil.which(h)}')

if __name__ == '__main__':
    config = Config()
