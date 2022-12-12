from FileOperations import *
from BlockCipherModes import * 
from DES_encryption import encrypt
from DES_encryption import createRoundKeys
from UserInterface import *


key = stringToBinary('testtest')
content = readFileContent(fileName)
binaryCypherText = []
plainText = []
initializationVector = ''

if initializationVector == '' and not decryption:
    initializationVector = generateInitializationVector()

content = checkIfBinary(content)

roundKey = createRoundKeys(key,decryption)
initalBinaryInitializationVector = stringToBinary(initializationVector)

binaryInitializationVector = stringToBinary(initializationVector) #convert to initialization vector to binary

initalBinaryPlainText = content
fullBinaryPlainText = addPaddingToBinaryPlainText(initalBinaryPlainText)

binaryPlainTextArray = splitIn64Bits(fullBinaryPlainText) #splits it and returns array
#initializationVector <-save this somewhere idk
for binaryPlainText in binaryPlainTextArray:
    if decryption:
        binaryCBCText = encrypt(binaryPlainText,roundKey)
        plainText.append(xor(binaryCBCText,initalBinaryInitializationVector))
        initalBinaryInitializationVector = binaryPlainText
    else:
        binaryCBCText = xor(binaryPlainText,initalBinaryInitializationVector)
        binaryCypherText.append(encrypt(binaryCBCText,roundKey))
        initalBinaryInitializationVector = binaryCBCText

if decryption:
    writeContentToFile(binaryToString(removePaddingToBinaryPlainText
                                      (arrayToString(plainText))),
                       fileName)
else:
    writeContentToFile(arrayToString(binaryCypherText),fileName)
