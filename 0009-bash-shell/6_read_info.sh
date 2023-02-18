# !/bin/bash
# Programa para ejemplificar la lectura de información del usuario
# Autor: cogdiver

name=""
lastname=""
age=0

echo "Information Reading Program"
echo -n "What is your name? "
read
name=$REPLY
read -p "What is your lastname? " lastname
echo -n "How old are you? "
read age

echo "$name $lastname, you are $age years old"

