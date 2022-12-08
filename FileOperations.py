import os
from BlockCipherModes import stringToBinary 

def readFileContent(file_name):
    file = open(os.path.join(f'{file_name}'),'r')
    data = file.read().rstrip()
    file.close()
    return data
    
def checkIfBinary(data):
    binary_example = '10'
    count = 0
    for char in data:
        if char not in binary_example:
            count = 1
            break
        else:
            pass
    if count:
        return stringToBinary(data)
    else:
        return data
    
def writeContentToFile(content, file_name):
    file = open(os.path.join(f'{file_name}'),'w')
    file.seek(0)
    file.write(content)
    file.truncate()

