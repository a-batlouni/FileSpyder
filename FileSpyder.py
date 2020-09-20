import os

dirContent = os.listdir()

def makeDict():
    dirContent=os.listdir()
    dirLength=list(range(len(dirContent)))
    dirDict=dict(zip(dirLength,dirContent))
    print(dirDict)
    
    
'''
os.chdir("/Users/admin")
Convert()
print(dir_dict)
'''

makeDict()


