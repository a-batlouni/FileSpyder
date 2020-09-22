import os
import pathlib


class Spyder:
    def __init__(self, path):
        self.path = path
        self.dirDict = None
        self.fileType = ""
        self.hitList = []

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

# next step is to print the dirs in the current working directory, and ask user if filespyder should continue crawling
#   if yes, restart processes (makeDict(), crawl())
#   if no, retrieve current hitList files
