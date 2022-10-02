#!/usr/bin/env python
import bcrypt
import sys
import numpy as np
from numba import jit

''' TODO
// get file from args 
// loop through each line and hash value, 
    store to hashmap with hashed value as key, plaintext as value
// wrap functions with cuda lib
// clean up
'''

# only emable with NVIDIA Card 
#@jit
def hash(inputFile):
    for line in inputFile:
        salt = bcrypt.gensalt() ## temp fix, not sure how I could make this useful without reading in salts and trying each combo
        hashedValue = bcrypt.hashpw(line.encode(), salt)
        table.update({line:hashedValue})
    return table

if __name__ == "__main__":
    
    table={}

    inputFile = open(sys.argv[1], 'r')
    #saltFile = open(sys.argv[2], 'r')
    #outputFile=open(sys.argv[3], 'r')
    hashTable = hash(inputFile)

    for key in hashTable:
        print(key)
        print(hashTable[key])
        print("\n")
        