import platform
import os

class Settings:
    def __init__(self):
        self.os = platform.system()
        home = os.path.expanduser('~')

        if self.os == 'Windows':
            self.ruta = os.path.join(home, '_vimrc')
        else:
            self.ruta = os.path.join(home, '.vimrc')

    def vim(self):
        return [
            'syntax on',
            'set t_Co=256',
            'set background=dark',
            '',
            'set number',
            'set relativenumber', 
            'set cursorline',
            '',
            'set mouse=a',
            'set expandtab',
            'set tabstop=4',
            'set shiftwidth=4',
            '',
            'set autoindent',
            'set noswapfile',
            'set nobackup',
            '"   --- Comandos ---',
            '"nnoremap <leader>w :w<CR>'
        ]

    def latex(self):
        return [
            r'\documentclass{article}',
            r'\usepackage[spanish]{babel}',
            r'\usepackage[margin=2.5cm]{geometry}',
            r'\usepackage{amsmath, amssymb}',
            r'\usepackage{graphicx}',
            r'\usepackage{hyperref}',
            r'\begin{document}',
            r'',
            r'\end{document}'
        ]

    def show(self):
        vim = self.vim()
        with open(self.ruta, 'w') as files:
            files.write('\n'.join(vim))
        print(f'Sistema: {self.os}')
        print(f'Vimrc: {self.ruta}')

if __name__ == '__main__':
    settings = Settings()
    settings.show()
