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
# note weird syntax here^
# because the first bit is all the way to the left in
# the array, but needs to be all the way to the right
# in the string - this dynamic shows up several times
# in this program.
    return byteString

# takes 0-7 as an argument and returns the
# corresponding bit as a zero or a one (string)
def getBit(i):
    return str(int(bitArray[i]))

# returns the decimal value of the byte
def getDec():
    byteNumber = 0
    for i in range(8):
        byteNumber += 2**i*bitArray[i]
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

# right-shifts the byte
def rightShift():
    del bitArray[0]    
    bitArray.append(False)

# left-shifts the byte
def leftShift():
    bitArray.pop()
    bitArray.insert(0, False)

# sets the byte equal to a given integer
def setFromNum(num):
    for i in range(8):
        bitArray[i] = bool(num & 1<<i)

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
