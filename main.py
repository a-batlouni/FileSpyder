import os

#def getPath():

data = None
path = None

def makeDict():
    dirContent=os.listdir(path)
    dirLength=list(range(len(dirContent)))
    data=dict(zip(dirLength,dirContent))
    return(data)

print(makeDict())


