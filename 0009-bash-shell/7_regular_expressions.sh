# !/bin/bash
# Program to ejemplify the use of regular expressions
# Autor: cogdiver

Rage='^[0-9]{,3}$'
Rcc='^[0-9]{10}$'
Rname='^\w{1,20}$'

echo "Regular Expressions Program"
read -p "What is your name? " name
read -p "How old are you? " age
read -p "What is your identification number? " cc

# Name validation
if [[ $name =~ $Rname ]]; then
  echo "Valid name $name"
else
  echo "Invalid name $name"
fi

# Identify validation
if [[ $age =~ $Rage ]]; then
  echo "Valid age $age"
else
  echo "Invalid age $age"
fi

# Identify validation
if [[ $cc =~ $Rcc ]]; then
  echo "Valid identification number $cc"
else
  echo "Invalid identification number $cc"
fi
