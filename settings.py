import os, platform, shutil

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
    software = ["vim", "git", "gcc", "pdflatex", "python3"]
    print(f"{'software':<15} {'version'}")
    print(f"{'-'*30}")

    for i in software:
        version = shutil.which(i)
        print(f"{i:<15} {version}")


print(f"Sistema: {sistem}")
software()
