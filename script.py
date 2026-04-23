import os
import platform
import subprocess

def configurar_estilos_vim():
    sistema = platform.system()
    home = os.path.expanduser("~")
    
    # Definir el nombre del archivo según el sistema
    archivo_vim = os.path.join(home, "_vimrc" if sistema == "Windows" else ".vimrc")

    # --- AQUÍ AGREGAS TUS ESTILOS Y CONFIGURACIONES ---
    estilos = [
        '" --- Personalización Visual ---',
        'syntax on',                   # Activa colores de código
        'colorscheme desert',          # Cambia esto por tu tema favorito
        'set number',                  # Muestra números de línea
        'set relativenumber',          # Números relativos (útil para saltar líneas)
        'set cursorline',              # Resalta la línea actual
        '',
        '" --- Comportamiento ---',
        'set clipboard=unnamedplus',   # Permite pegar desde afuera con 'p'
        'set mouse=a',                 # Habilita el ratón
        'set tabstop=4',               # Tamaño de pestaña
        'set shiftwidth=4',
        'set expandtab',               # Usa espacios en lugar de pestañas
        '',
        '" --- Atajos de compilación ---',
        'nnoremap <F5> :w<CR>:!pdflatex %<CR>', # Compilar LaTeX con F5
    ]

    try:
        with open(archivo_vim, "w", encoding="utf-8") as f:
            f.write("\n".join(estilos))
        print(f"🎨 Estilos de Vim instalados en: {archivo_vim}")
    except Exception as e:
        print(f"❌ Error al configurar estilos: {e}")

def auto_instalar_en_path():
    sistema = platform.system()
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    print(f"⚙️  Configurando acceso global desde: {ruta_actual}")

    if sistema == "Windows":
        try:
            path_actual = os.environ.get('PATH', '')
            if ruta_actual not in path_actual:
                # Usamos /M si quisiéramos PATH de sistema, pero para usuario está bien así
                subprocess.run(['setx', 'PATH', f'{path_actual};{ruta_actual}'], check=True)
                print("✅ Carpeta añadida al PATH de Windows.")
            else:
                print("ℹ️  La carpeta ya está en el PATH.")
        except Exception as e:
            print(f"❌ Error al modificar PATH: {e}")

    elif sistema in ["Linux", "Darwin"]:
        shell_config = os.path.expanduser("~/.bashrc")
        if os.path.exists(os.path.expanduser("~/.zshrc")):
            shell_config = os.path.expanduser("~/.zshrc")

        linea_path = f'\nexport PATH="$PATH:{ruta_actual}"\n'
        try:
            with open(shell_config, "a+") as f:
                f.seek(0)
                if ruta_actual not in f.read():
                    f.write(linea_path)
                    print(f"✅ PATH añadido a {shell_config}.")
                else:
                    print("ℹ️  La carpeta ya está en la configuración de Shell.")
        except Exception as e:
            print(f"❌ Error al modificar Shell: {e}")

# --- PUNTO DE EJECUCIÓN ---
if __name__ == "__main__":
    # Primero configuramos Vim
    configurar_estilos_vim()
    
    # Luego nos aseguramos de que el script sea global
    auto_instalar_en_path()
    
    print("\n✨ ¡Configuración completa! Reinicia tu terminal para ver los cambios.")
