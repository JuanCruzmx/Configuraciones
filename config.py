import os
import platform
import shutil

class Config:
    def __init__(self):
        self.os = platform.system()         # Detección del sistema
        self.home = os.path.expanduser("~")      # Busca carpeta de usuario
        self.herramientas = ['vim', 'git', 'pdflatex', 'python3', 'gcc', 'g++', 'dotnet', 'java', 'javac']    
        self.tema = 'desert'
        if self.os == 'Windows':
            self.nombre_vim = '_vimrc'
            self.abrir_pdf = '!start chrome "%:r.pdf"'
            self.ejecutar = ''
            self.ext = '.exe'
            self.borrar = 'del'
            self.unir = '&'
        elif self.os == 'Darwin':
            self.nombre_vim = '.vimrc'
            self.abrir_pdf = '!open -a "Google Chrome" "%:r.pdf"'
            self.ejecutar = './'
            self.ext = ''
            self.borrar = 'rm -f'
            self.unir = '&&'
        else:
            self.nombre_vim = ".vimrc"
            self.abrir_pdf = '!explorer.exe "%:r.pdf"'
            self.ejecutar = './'
            self.ext = ''
            self.borrar = 'rm -f'
            self.unir = '&&'
        self.ruta_vim = os.path.join(self.home, self.nombre_vim)

    def plantilla_latex(self):
        return [
            r'\documentclass{article}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[spanish]{babel}',
            r'\usepackage{amsmath, amssymb}',
            r'\usepackage{graphicx}',
            r'\usepackage[margin=2.5cm]{geometry}',
            r'\usepackage{hyperref}',
            r'\setlength{\parindent}{0pt}',
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
        plantilla = self.plantilla_latex()
        return [
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
            f'autocmd BufEnter *.tex nnoremap <buffer> <C-c> :w<CR>:!pdflatex % {self.unir} {self.borrar} "%:r.aux" "%:r.log" "%:r.out"<CR>:{self.abrir_pdf}<CR><CR>',
            f'autocmd BufEnter *.c nnoremap <buffer> <C-c> :w<CR>:!gcc % -o %< {self.unir} {self.ejecutar}%<{self.ext}<CR>',
            f'autocmd BufEnter *.cpp nnoremap <buffer> <C-c> :w<CR>:!g++ % -o %< {self.unir} {self.ejecutar}%<{self.ext}<CR>',
            f'autocmd BufEnter *.cs nnoremap <buffer> <C-c> :w<CR>:!dotnet run<CR>',
            '"  --- Funciones ---',
            'function! PlantillaLatex()',
            *[f"    call setline({i+1}, '{linea.replace(chr(39),chr(39)+chr(39))}')" for i, linea in enumerate(plantilla)],
            '   execute "normal! 15G" | startinsert',
            'endfunction',
            'autocmd BufNewFile *.tex call PlantillaLatex()',
        ]

    def aplicar(self):
        vim = self.config_vim()
        with open(self.ruta_vim, 'w', encoding='utf-8') as f:
            f.write("\n".join(vim))
        verificar = [('[ OK ]' if shutil.which(h) else '[ FAILED ]', h, shutil.which(h) or '---') for h in self.herramientas]
        print(f'\n{("[ OK ]" if os.path.exists(self.ruta_vim) else "[ FAILED ]").ljust(10)} {"vimrc".ljust(13)} {self.ruta_vim}')
        for sta, h, ruta in verificar:
            print(f'{sta.ljust(10)} {h.ljust(13)} {ruta}')
        print(f'\n[SUCCESS] Se aplicarón las configuraciones en {self.os}')

if __name__ == '__main__':
    config = Config()
    config.aplicar()
