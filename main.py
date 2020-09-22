import os
import pathlib


class Spyder:
    def __init__(self, path):
        self.path = path
        self.dirDict = None
        self.fileType = ""
        self.hitList = []
        self.dirList = []

    def makeDict(self):
        emptyList = []
        # Returns contents of current working dir
        dirList = os.listdir(self.path)
        # Checks to see if each content of working dir is a dir
        for contents in dirList:
            emptyList.append(os.path.isdir(contents))
        # Combines lists to create dictionary with file name as key and isDir as value
        self.dirDict = dict(zip(dirList, emptyList))
        print(self.dirDict)
        return (self.dirDict)

    def crawl(self):
        for key, value in self.dirDict.items():
            if value is True:
                print(key + ' is a dir')
                self.dirList.append(key)
            else:
                print(key + ' is a file')
                if key.endswith(self.fileType):
                    self.hitList.append(key)
        print(self.hitList)

    def fileExtension(self):
        prompt = "Enter desired file extension"
        self.fileType = input(prompt)


x = Spyder(".")
x.fileExtension()
x.makeDict()
x.crawl()
# add matching files, list dirs
# os.chdir & print(os.path.abspath("."))
