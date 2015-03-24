#!/usr/bin/python

storageFile = "./stuff_remebered.txt"

def storeThis(toStore):
    print toStore
    f.open(storageFile,'w')
    f.write(toStore)
    
