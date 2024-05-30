# !/bin/bash
# programa para revisar como ejecutar comando dentro de un programa y almacenar en una variables
# Autor: cogdiver

u=`pwd`
info=$(uname -a)

echo "Ubicacion actual: $u"
echo "informacion de kernel: $info"
