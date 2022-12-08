import string
import random

#return spit 64-bit binary text
def splitIn64Bits(binaryText):
    return [binaryText[bit:bit+64] for bit in range(0, len(binaryText), 64)]

def arrayToString(array):
    return ''.join(element for element in array)

#Convert string to binary
def stringToBinary(string):
    return ''.join(format(ord(byte), '08b') for byte in string)

#convert binary to string
def binaryToString(binary):
    string = ""
    for i in range(0, len(binary), 8):
        binarySplitIn8bit = binary[i:i + 8]
        decimal = int(binarySplitIn8bit, 2)
        string = string + chr(decimal)
    return string

#xor two binary numbers
def xor(binaryText, binaryInitializationVector):
	xor = ""
	for i in range(len(binaryText)):
		if (binaryText[i] == binaryInitializationVector[i]):
			xor += "0"
		else:
			xor += "1"
	return xor

#returns binary plain text that can be used by DES
def addPaddingToBinaryPlainText(binaryPlainText,plainText):
    while(len(binaryPlainText)%64!=0):
        if(len(stringToBinary(plainText))==len(binaryPlainText)):
            binaryPlainText = binaryPlainText + "10000000"
        else:
            binaryPlainText = binaryPlainText + "0"
    return binaryPlainText

def removePaddingToBinaryPlainText(binaryPlainText):
    return binaryPlainText[:binaryPlainText.rfind('1')]

def generateInitializationVector():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(8))

#everything below this are notes

#encryption
__plainText = "I love Among Us"
__initializationVector = generateInitializationVector()
__binaryCypherTextArray = []

__binaryPlainText = stringToBinary(__plainText) #convert to plain text to binary
__fullBinaryPlainText = addPaddingToBinaryPlainText(__binaryPlainText,__plainText) #add extra bits to make it size%64==0
__binaryPlainTextArray = splitIn64Bits(__fullBinaryPlainText)#splits it and returns array
__binaryInitializationVector = stringToBinary(__initializationVector)#convert to initialization vector to binary
#__initializationVector <-save this somewhere idk
for binaryPlainText in __binaryPlainTextArray:
    __binaryCypherText = xor(binaryPlainText,__binaryInitializationVector)
    __binaryCypherTextArray.append(__binaryCypherText)
    __binaryInitializationVector = __binaryCypherText

#decryption
removePaddingToBinaryPlainText(__fullBinaryPlainText)

