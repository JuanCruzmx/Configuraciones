@echo off

set "CUR_DIR=%cd:\=/%"

echo " Configuracion de Juan Cruz" > "%USERPROFILE%\_vimrc"
echo source %CUR_DIR%/.vimrc >> "%USERPROFILE%\_vimrc"

set "PLANTILLA=%CUR_DIR%/Config-Latex/plantilla.tex"

echo autocmd BufNewFile *.tex 0read %PLANTILLA% ^| set filetype=tex >> "%USERPROFILE%\_vimrc"

echo Instalación completada...
echo Plantilla Latex completada...

pause
