import os, platform, shutil, subprocess, sys, re

sistem = platform.system()
home = os.path.expanduser("~") 

if sistem == "Windows":
    vim = os.path.join(home, "_vimrc")
    delete = "del /Q"
elif sistem == "Darwin":
    vim = os.path.join(home, ".vimrc")
    delete = "rm -f"
else:
    vim = os.path.join(home, ".vimrc")
    delete = "rm -f"

def software():
    software = ["vim", "git", "gcc", "pdflatex", "python3", "java"]
    print(f"{'software':<15}{'version'}")
    print(f"{'-'*30}")

    for i in software:
        verificar = shutil.which(i)
        version = subprocess.run([i, "--version"], capture_output=True, text=True, check=True)
        if not verificar:
            print(f"{i}")
            continue
        else:
            print(f"{i:<15}{re.search(r'\d+(\.\d+)+', version.stdout.splitlines()[0]).group(0)}")

intentos = 1
print(f"Sistema: {sistem}")
while True:
    opcion = input("Ver software instalados [Y/N]: ").upper()
    if opcion == "Y":
        software()
        break
    elif opcion == "N":
        break 
    else:
        if intentos == 3:
            sys.exit()
        intentos += 1
