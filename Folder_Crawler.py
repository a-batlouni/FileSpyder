import os

dirContent = os.listdir()

def makeLists():
    dirContent=os.listdir()
    dirLength=list(range(len(dirContent)))
    test=dict(zip(dirLength,dirContent))
    '''print(dirContent)
    print(dirLength)'''
    print(test)
    

def Convert(): 

    dirContent = os.listdir()
    dir_dict = {dirContent[i]: dirContent[i + 1] for i in range(0, len(dirContent), 2)} 
    return dir_dict 
'''

os.chdir("/Users/admin")
Convert()
print(dir_dict)
'''

makeLists()


