#!/usr/bin/python3

import sys


max=0.0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
#    data_mapped = line.strip().split("\t")
#    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
#       continue

    #thisCost = data_mapped

    if float(line) > max:
    	max =float(line)

    
   

# Escribe o último par, unha vez rematado o bucle
print(max)