from FileOperations import *
from BlockCipherModes import * 
from DES_encryption import encrypt
from DES_encryption import createRoundKeys
from UserInterface import decryption
from UserInterface import fileName

key = stringToBinary('testtest')
content = readFileContent(fileName)
binaryCypherText = []
PlainText = []
initializationVector = ''

if initializationVector == '' and not decryption:
    initializationVector = generateInitializationVector()
    print(initializationVector)

content = checkIfBinary(content)

roundKey = createRoundKeys(key,decryption)
initalBinaryInitializationVector = stringToBinary(initializationVector)

binaryInitializationVector = stringToBinary(initializationVector) #convert to initialization vector to binary
if not decryption:
    content = addPaddingToBinaryPlainText(content)

binaryPlainTextArray = splitIn64Bits(content) #splits it and returns array
#initializationVector <-save this somewhere idk
for binaryPlainText in binaryPlainTextArray:
    if decryption:
        binaryCBCText = encrypt(binaryPlainText,roundKey)
        PlainText.append(xor(binaryCBCText,initalBinaryInitializationVector))
        initalBinaryInitializationVector = binaryPlainText
    else:
        binaryCBCText = xor(binaryPlainText,initalBinaryInitializationVector)
        initalBinaryInitializationVector = encrypt(binaryCBCText,roundKey)
        binaryCypherText.append(initalBinaryInitializationVector)
if decryption:
    writeContentToFile(binaryToString(removePaddingToBinaryPlainText
                                      (arrayToString(PlainText))),
                       fileName)
else:
    writeContentToFile(arrayToString(binaryCypherText),fileName)