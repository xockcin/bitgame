# game plan:
# 1. Have a list of all the numbers from 0 to 255.
# 2. For each number in the list, attach to it five properies, one for the result of each of the five operators upon that number.
# 3. That gets you all the one-steppers.

import bitgame_proto as bg

def do_number(i):
    number = {}
    byte = bg.byteFromNum(i)
    cmp = bg.returnComplement(byte)
    lsh = bg.returnLeftShift(byte)
    rsh = bg.returnRightShift(byte)
    number["n"] = i
    number["+"] = i + 1
    number["-"] = i - 1
    number["~"] = bg.getDecFromByte(cmp)
    number["<"] = bg.getDecFromByte(lsh)
    number[">"] = bg.getDecFromByte(rsh)
    return number