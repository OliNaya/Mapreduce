#!/usr/bin/python3

import sys

diccionario={}
oldKey = None
oldPagos=0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCost = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if not thisKey in diccionario: #metemos la clave que e o tipo de tarjeta
    	diccionario[thisKey]=thisCost #metemos o valor
    	
    else:
    	oldPagos=diccionario[thisKey]
    	if  float(oldPagos) < float(thisCost): #metemos la clave si es menor a la otra
    	  #diccionario.update({'{}'.format(thisKey): float (thisCost)})3
    	  diccionario.update({thisKey: float (thisCost)})
   

# Escribe o último par, unha vez rematado o bucle
for d in diccionario:
    print(d,diccionario[d])