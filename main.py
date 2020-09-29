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

def moveFiles(path=sys.argv[1], destination=sys.argv[3], options=None):
    if len(sys.argv) == 5:
        options = sys.argv[4]
    else:
        options = None
    if os.path.exists(destination):
        basename = []
        destination = str(os.path.abspath(destination))
        for file in List_file:
            basename.append(os.path.basename(file))
        #destination = [destination + "/" + file for file in basename]
        if options == "-force":
            for file_name in List_file:
                shutil.move(os.path.join(path, file_name), destination)
            print("The files" + "\n" + "\n" + str('\n'.join([str(i) for i in List_file])) + "\n" + "\n" + "have been moved to " + "\n" + "\n" + str(destination))
        elif options is None:
            while True:
                confirmation = input("You are about to move the following files:" + "\n" + "\n" + str('\n'.join([str(i) for i in List_file])) + "\n" + "\n" + "To this destination:" + "\n" + "\n" + str(destination) + "\n" + "\n" + "Are you sure you want to do this?" + "\n")
                if confirmation.lower() == "y" or confirmation.lower() == "yes":
                    for file_name in List_file:
                        shutil.move(os.path.join(path, file_name), destination)
                    print("\n" + "The files:" + "\n" + "\n" + str('\n'.join([str(i) for i in List_file])) + "\n" + "\n" + "Have been moved to:" + "\n" + "\n" + str(destination))
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

getFiles()
moveFiles()