import os, platform, shutil, subprocess, sys, re

sistema = platform.system()
home = os.path.expanduser("~") 
ruta_actual = os.getcwd()
plantillas = os.path.join(ruta_actual, "Plantillas")

if sistema == "Windows":
    vimrc = os.path.join(home, "_vimrc")
    vim = os.path.join(home, "vimfiles")
    delete = "del /Q"
    open_pdf = "start '' '%:r.pdf'"
elif sistema == "Darwin":
    vimrc = os.path.join(home, ".vimrc")
    vim = os.path.join(home, ".vim")
    delete = "rm -f"
    open_pdf = "open '%:r.pdf'"
else:
    vimrc = os.path.join(home, ".vimrc")
    vim = os.path.join(home, ".vim")
    delete = "rm -f"
    open_pdf = "powershell.exe -c start '%:r.pdf'"

def software():
    software = ["vim", "git", "gcc", "pdflatex", "python3", "java"]
    print(f"{'software':<15}{'version'}")
    print(f"{'-'*30}")

    for i in software:
        verificar = shutil.which(i)
        if not verificar:
            print(f"{i}")
            continue
        try:
            version = subprocess.run([i, "--version"], capture_output=True, text=True, check=True)
            print(f"{i:<15}{re.search(r'\d+(\.\d+)+', version.stdout.splitlines()[0]).group(0)}")
        except Exception:
            print(f"{i}")

def compilar_latex():
    with open("vim", "r", encoding="utf-8") as l:
        linea = l.readlines()
    linea[27] =  f"autocmd BufRead,BufNewFile *.tex nnoremap <buffer> <C-b> :w<CR>:silent !pdflatex -interaction=nonstopmode '%' && {delete} '%:r.log' '%:r.aux' '%:r.out' '%:r.pyg' && {open_pdf} <CR>:redraw!<CR>" + "\n"
    with open("vim", "w", encoding="utf-8") as l:
        l.writelines(linea)

def Vim():
    home_plantillas = os.path.join(vim, "Plantillas")
    if os.path.lexists(vimrc):
        os.remove(vimrc)
    if os.path.lexists(home_plantillas):
        if os.path.islink(home_plantillas) or os.path.isfile(home_plantilas):
            os.remove(home_plantillas)
        else:
            shutil.rmtree(home_plantillas)
    os.symlink(os.path.join(ruta_actual, "vim"), vimrc)
    os.symlink(plantillas, home_plantillas)

intentos = 1
print(f"Sistema: {sistema}")
while True:
    opcion = input("Ver software instalados [Y/N]: ").upper()
    if opcion == "Y":
        compilar_latex()
        software()
        Vim()
        print("Configuraciones listas...")
        break
    elif opcion == "N":
        break 
    else:
        if intentos == 3:
            sys.exit()
        intentos += 1
