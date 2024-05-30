# !/bin/bash
# Programa para revisar los tipos de operadores
# Autor: cogdiver

numA=10
numB=4

echo "Operadores aritméticos"
echo "Números A=$numA , B=$numB"
echo "Sumar A+B="$((numA + numB))
echo "Restar A-B="$((numA - numB))
echo "Multiplicar A*B="$((numA * numB))
echo "Dividir A/B="$((numA / numB))
echo "Residuo A%B="$((numA % numB))

echo  "------------------------------------------"

echo "Operadores relacionales"
echo "Números A=$numA , B=$numB"
echo "A > B="$((numA > numB))
echo "A < B="$((numA < numB))
echo "A == B="$((numA == numB))
echo "A != B="$((numA != numB))
echo "A >= B="$((numA >= numB))
echo "A <= B="$((numA <= numB))

echo  "------------------------------------------"

x=10
y=4
echo "BASIC ASSIGNATION OPERATORS"
echo "Números x=$x , y=$y"
echo "x += y :" $((x +=y ))
echo "x -= y :" $((x -=y ))
echo "x *= y :" $((x *=y ))
echo "x /= y :" $((x /=y ))
echo "x %= y :" $((x %=y ))
