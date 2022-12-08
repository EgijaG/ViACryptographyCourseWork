from FileOperations import *
from BlockCipherModes import * 
from DES_encryption import encrypt
from DES_encryption import createRoundKeys

Decryption = True
fileName = ''
key = stringToBinary('testtest')
content = readFileContent(fileName)
binaryCypherText = []
PlainText = []
initializationVector = ''

if initializationVector == '' and not Decryption:
    initializationVector = generateInitializationVector()

content = checkIfBinary(content)

roundKey = createRoundKeys(key,Decryption)
initalBinaryInitializationVector = stringToBinary(initializationVector)

binaryInitializationVector = stringToBinary(initializationVector) #convert to initialization vector to binary

initalBinaryPlainText = content
fullBinaryPlainText = addPaddingToBinaryPlainText(initalBinaryPlainText)

binaryPlainTextArray = splitIn64Bits(fullBinaryPlainText) #splits it and returns array
#initializationVector <-save this somewhere idk
for binaryPlainText in binaryPlainTextArray:
    if Decryption:
        binaryCBCText = encrypt(binaryPlainText,roundKey)
        PlainText.append(xor(binaryCBCText,initalBinaryInitializationVector))
        initalBinaryInitializationVector = binaryPlainText
    else:
        binaryCBCText = xor(binaryPlainText,initalBinaryInitializationVector)
        binaryCypherText.append(encrypt(binaryCBCText,roundKey))
        initalBinaryInitializationVector = binaryCBCText

if Decryption:
    writeContentToFile(binaryToString(removePaddingToBinaryPlainText
                                      (arrayToString(PlainText))),
                       fileName)
else:
    writeContentToFile(arrayToString(binaryCypherText),fileName)
