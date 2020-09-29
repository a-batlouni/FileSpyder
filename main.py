#!/usr/bin/python3

import os
import sys
import shutil

List_dir = []
List_file = []

def getFiles(path=sys.argv[1], extension=sys.argv[2]): 
    if os.path.exists(path):
        path = os.path.abspath(path)
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                if name.endswith(extension):
                    List_file.append((os.path.join(root, name)))
            for name in dirs:
                    List_dir.append(os.path.join(root, name))       
    else:
        raise ValueError('The path does not exist')    
    print(List_file)

def moveFiles(path=sys.argv[1], destination=sys.argv[3], options=sys.argv[4]):
    if os.path.exists(destination):
        basename = []
        destination = str(os.path.abspath(destination))
        for file in List_file:
            basename.append(os.path.basename(file))
        #destination = [destination + "/" + file for file in basename]
        if options == "-force":
            for file_name in List_file:
                shutil.move(os.path.join(path, file_name), destination)
        elif options is None:
            while True:
                confirmation = input("Are you sure?")
                if confirmation.lower() == "y" or confirmation.lower() == "yes":
                    for file_name in List_file:
                        shutil.move(os.path.join(path, file_name), destination)
                    break
                elif confirmation.lower() == "n" or confirmation.lower() == "no":
                    print("Program terminated.")
                    pass  
                    break
                else:         
                    print("Please answer Yes[Y] or No[N]")
        else:
            raise ValueError('That argument is not recognized. Please use -force to disregard safety; otherwise, do not add an option.')    
    else:
        raise ValueError('The destination path does not exist')    

    print(List_file)
    print(destination)

getFiles()
moveFiles()