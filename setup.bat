@echo off
echo ===== Intalador de Configuraciones de Juan Cruz para Vim =====
set REPO_PATH=%cd%
set VIMRC_FILE=%REPO_PATH%\.vimrc

set VIMRC_CONTENT=source %VIMRC_FILE:\=/%

echo %VIMRC_CONTENT% > "%USERPROFILE%\_vimrc"

echo Instalación completada...
echo Configuraciones y estilos listos para Vim en tu sistema...

pause
