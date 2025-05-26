def TenToTwo(decimal):
    baseTwo = ''
    if decimal == 0: 
        return '0'
    while decimal > 0: 
        baseTwo = str(decimal % 2) + baseTwo
        decimal //= 2
    return baseTwo
def TwoToTen(binary):
    sum = 0
    result = ''
    binaryStr = str(binary)
    wholeStr, period, decimalStr = binaryStr.partition('.')
    lstWhole = []
    for i in range(0,len(wholeStr)): 
        lstWhole.append(int(wholeStr[i]))
    maxIndex = len(lstWhole) - 1
    for value in lstWhole: 
        sum += value * (2 ** maxIndex)
        maxIndex -= 1
    whole = sum
    sum = 0
    lstDec = []
    for i in range(0,len(decimalStr)): 
        lstDec.append(int(decimalStr[i]))
    maxIndex = -1
    for value in lstDec: 
        sum += value * (2 ** maxIndex)
        maxIndex -= 1
    dec = sum % 1
    result += str(dec)
    return whole + dec

numB = 101101
print("Decimal of", numB, ":", TwoToTen(numB))
numW = 45
print("Binary of", numW, ":", TenToTwo(numW))    
numB = 1100011
print("Decimal of", numB, ":", TwoToTen(numB))
numW = 99
print("Binary of", numW, ":", TenToTwo(numW))   