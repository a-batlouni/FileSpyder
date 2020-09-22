import os
import pathlib

class Spyder:
    def __init__(self, path):
        self.path=path
        self.dirDict=None

    def makeDict(self):
        emptyList=[]
        # Returns contents of current working dir
        dirList = os.listdir(self.path)
        # Checks to see if each content of working dir is a dir
        for contents in dirList:
            emptyList.append(os.path.isdir(contents))
        # Combines lists to create dictionary with file name as key and isDir as value
        self.dirDict=dict(zip(dirList,emptyList))
        print(self.dirDict)
        return(self.dirDict)
    
    def crawl(self):
        for key, value in self.dirDict.items():
            if value is True:
                print(key + ' is a dir')
            else:
                print(key + ' is a file')
        
x = Spyder(".")
x.makeDict()
x.crawl()


