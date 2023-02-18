# !/bin/bash
# Programa para ejemplificar el paso de argumentos

nombrePrograma=$0
nombreCurso=$1
horarioCurso=$2

echo "Nombre del programa: $nombrePrograma"
echo "Nombre del curso: $nombreCurso"
echo "Horario del curso: $horarioCurso"
echo "Número de argumentos: $#"
echo "Argumentos: $*"
