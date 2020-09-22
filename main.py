import os


def dirDict(path):
    emptyList=[]
    # Returns contents of current working dir
    dirList = os.listdir(path)
    # Checks to see if each content of working dir is a dir
    for contents in dirList:
        emptyList.append(os.path.isdir(contents))
    # Combines lists to create dictionary with file name as key and isDir as value
    dirDict=dict(zip(dirList,emptyList))
    return(dirDict)


print(dirDict("."))



