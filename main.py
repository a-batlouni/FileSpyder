#!/usr/bin/python

import os
import sys
import shutil

List_dir = []
List_file = []

def getFiles(path=sys.argv[1], extension=sys.argv[2]): 
    path = os.path.abspath(path)
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.endswith(extension):
                List_file.append((os.path.join(root, name)))
        for name in dirs:
                List_dir.append(os.path.join(root, name))        
    print(List_file)

def moveFiles(path=sys.argv[1], destination=sys.argv[3]):
    basename = []
    destination = str(os.path.abspath(destination))
    for file in List_file:
        basename.append(os.path.basename(file))
    #destination = [destination + "/" + file for file in basename]
    for file_name in List_file:
        shutil.move(os.path.join(path, file_name), destination)
    print(List_file)
    print(destination)

getFiles()
moveFiles()