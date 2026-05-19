import platform
import shutil
import os
import sys
import subprocess
import re

class Settings:
    def __init__(self):
        self.os = platform.system()
        home = os.path.expanduser("~")

        if self.os == "Windows":
            self.ruta = os.path.join(home, "_vimrc")
            self.delete = "del /Q"
            self.open_pdf = "start '' '%:r.pdf'"
        else:
            self.ruta = os.path.join(home, ".vimrc")
            self.delete = "rm -f"
            self.open_pdf = "powershell.exe -c start '%:r.pdf'"

    def vim(self):
        return [
            "\"  --- UI Settings ---",
            "syntax on",
            "set number",
            "set relativenumber", 
            "set cursorline",
            "set mouse=a",
            "\"    --- Editing Settings ---",
            "set expandtab",
            "set tabstop=4",
            "set shiftwidth=4",
            "set clipboard=unnamedplus",
            "set autoindent",
            "set noswapfile",
            "set nobackup",
            "\"    --- Styles ---",
            "set t_Co=256",
            "set background=dark",
            "\"    --- Function ---",
            "function! Latex()",
            f"    call append(0, [{','.join(chr(39) + line + chr(39) for line in self.latex())}])",
            "    $d",
            "    normal! 13G",
            "endfunction",
            "function! README()",
            f"    call append(0, [{','.join(chr(39) + line + chr(39) for line in self.README())}])",
            "    $d",
            "    normal! 1G",
            "endfunction",
            "function! HTML()",
            f"    call append(0, [{','.join(chr(39) + line + chr(39) for line in self.html())}])",
            "    $d",
            "    normal! 9G",
            "endfunction",
            "\"    --- File identifier ---",
            "let mapleader = ' '",
            f"autocmd BufNewFile *.tex call Latex()",
            f"autocmd BufNewFile *.md call README()",
            f"autocmd BufNewFile *.html call HTML()",
            "\"    --- Keybindings ---",
            f"autocmd FileType tex nnoremap <buffer> <C-b> :w<CR>:!pdflatex -interaction=nonstopmode '%' <CR>:!{self.delete} '%:r.log' '%:r.aux' '%:r.out' <CR>:!{self.open_pdf}<CR>:redraw!<CR>"
        ]

    def latex(self):
        return [
            r"\documentclass{article}",
            r"\usepackage[spanish]{babel}",
            r"\usepackage[utf8]{inputenc}",
            r"\usepackage[margin=2.5cm]{geometry}",
            r"\usepackage{graphicx}",
            r"\usepackage{amsmath, amssymb}",
            r"\usepackage[hidelinks]{hyperref}",
            r"\usepackage{multicol}",
            r"\setlength{\parindent}{0pt}",
            fr"\title{{' . expand('%:t:r') . '}}",
            r"\author{Juan Cruz}",
            r"\date{\today}",
            r"\begin{document}",
            "",
            r"\end{document}"
        ]

    def html(self):
        return [
            "<!DOCTYPE html>",
            "<html lang=\"es\">",
            "<head>",
            "<meta charset=\"UTF-8\">",
            "    <link rel=\"stylesheet\" href=\"{{url_for()}}\">",
            "    <title></title>",
            "</head>",
            "<body>",
            "    <header>",
            "",
            "    </header>",
            "    <main>",
            "",
            "    </main>",
            "    <footer>",
            "        <p>© 2026</p>",
            "    </footer>",
            "</body>",
            "</html>"
        ]

    def README(self):
        return [
            "<h1> </h1>",
            "<p> </p>"
           ] 

    def package(self):
        package = ["vim", "git", "pdflatex", "python3", "gcc", "java"]

        for app in package:
            ver = subprocess.check_output([shutil.which(app), "--version"], text=True, stderr=subprocess.STDOUT) 
            version = re.search(r"\d+(?:\.\d+)+", ver)
            if shutil.which(app):
                print(f"{app:<15} {version.group(0)}")
            else:
                print(f"{app:<15}")

    def show(self):
        vim = self.vim()
        with open(self.ruta, "w") as files:
            files.write('\n'.join(vim))
        print(f"Sistema: {self.os}")
        print(f"Vimrc: {self.ruta}")
        while True:
            a = input("See installed apps [Y/N]: ").upper()
            if a == "Y":
                print(f"{'Package':<15} {'Version':<15}")
                print(f"{'-'*15} {'-'*15}")
                self.package()
                break
            elif a in ["", "N"]:
                sys.exit()

if __name__ == "__main__":
    settings = Settings()
    settings.show()
