import os

'''class Spyder:
        def __init__(self):
            self.path = None
            self.data = None

'''
#def getPath():

data = None
path = None

def makeDict():
    dirContent=os.listdir(path)
    dirLength=list(range(len(dirContent)))
    data=dict(zip(dirLength,dirContent))
    return(data)

print(makeDict())


