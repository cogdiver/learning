# !/bin/bash
# Programa para revisar la declaración de variables

option=0
nombre=Valentina

echo "Opcion: $option y Nombre: $nombre"

# Exportar variables
export nombre

# Llamar al siguiente script
./2_variables_copy.sh
