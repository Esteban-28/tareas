#!/bin/bash

#En caso de que no funcione debe verificar si tiene mailutils y ssmtp instalado
#Y configurar el ssmtp para que lo envie desde su correo.

read -p "Ingresa un titulo: " tit
read -p "Escribe el mensaje: " msg

while IFS= read -r line
do
	mail -s "$tit" "$line" <<< "$msg"
done < email.txt
