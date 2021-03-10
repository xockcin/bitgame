#
# Back-end for bitgame
#

# array to store the byte
bitArray = [] 

# loop to initialize the byte
for i in range(8):
    bitArray.append(False) 

# print byte to output, just for the hell of it
print(bitArray)

# returns byte as a string of zeroes and ones
def getByte():
    byteString = ""
    for i in range(8):
        byteString = str(int(bitArray[i])) + byteString
    return byteString

# takes 0-7 as an argument and returns the
# corresponding bit as a zero or a one (string)
def getBit(i):
    return str(int(bitArray[i]))

# returns the decimal value of the byte array
def getDec():
    byteNumber = 0
    for i in range(8):
        byteNumber += 2**i*bitArray[i]
    return byteNumber

def getDecFromByte(byte):
    byteNumber = 0
    for i in range(8):
        byteNumber += 2**i*byte[i]
    return byteNumber

# returns the ASCII value of the byte
def getASCII():
    return chr(getDec())

# returns the hex value of the byte
def getHex():
    return hex(getDec())

# inverts all the bits in the byte
def complement():
    for i in range(8):
        bitArray[i] = not bitArray[i]

def returnComplement(byte):
    newByte = []
    for i in range(8):
        newByte.append(not byte[i])
    return newByte

# right-shifts the byte
def rightShift():
    del bitArray[0]    
    bitArray.append(False)
    
def returnRightShift(byte):
    newByte = byte[1:]
    newByte.append(False)
    return newByte

# left-shifts the byte
def leftShift():
    bitArray.pop()
    bitArray.insert(0, False)

def returnLeftShift(byte):
    newByte = byte[:-1]
    newByte.insert(0, False)
    return newByte

# sets the byte equal to a given integer
def setFromNum(num):
    for i in range(8):
        bitArray[i] = bool(num & 1<<i)
        
def byteFromNum(num):
    byte = []
    for i in range(8):
        byte.append(bool(num & 1<<i))
    return byte

# increments the byte
def increment():
    current = getDec()
    current += 1
    setFromNum(current)
    
# decrements the byte
def decrement():
    current = getDec()
    current -= 1
    setFromNum(current)

# switches a given bit in the byte
def switch(bit):
    bitArray[bit] = not bitArray[bit]
