from FileOperations import *
from BlockCipherModes import * 
from DES_encryption import encrypt
from DES_encryption import createRoundKeys

Decryption = True
fileName = 'test.txt'
key = stringToBinary('testtest')
content = readFileContent(fileName)
binaryCypherText = []
PlainText = []
initializationVector = '12345678'

if initializationVector == '' and not Decryption:
    initializationVector = generateInitializationVector()
    print(initializationVector)

content = checkIfBinary(content)

roundKey = createRoundKeys(key,Decryption)
initalBinaryInitializationVector = stringToBinary(initializationVector)

binaryInitializationVector = stringToBinary(initializationVector) #convert to initialization vector to binary
if not Decryption:
    content = addPaddingToBinaryPlainText(content)

binaryPlainTextArray = splitIn64Bits(content) #splits it and returns array
#initializationVector <-save this somewhere idk
for binaryPlainText in binaryPlainTextArray:
    if Decryption:
        binaryCBCText = encrypt(binaryPlainText,roundKey)
        PlainText.append(xor(binaryCBCText,initalBinaryInitializationVector))
        initalBinaryInitializationVector = binaryPlainText
    else:
        binaryCBCText = xor(binaryPlainText,initalBinaryInitializationVector)
        initalBinaryInitializationVector = encrypt(binaryCBCText,roundKey)
        binaryCypherText.append(initalBinaryInitializationVector)
if Decryption:
    writeContentToFile(binaryToString(removePaddingToBinaryPlainText
                                      (arrayToString(PlainText))),
                       fileName)
else:
    writeContentToFile(arrayToString(binaryCypherText),fileName)