#!/usr/bin/python

storageFile = "./stuff.txt"

def storeThis(toStore):
    print toStore
    file = open(storageFile,'a')
    file.write(toStore+'\n')
    file.close()

def showStored():
    file = open(storageFile,'r')
    return str(file.read())
    file.close()
