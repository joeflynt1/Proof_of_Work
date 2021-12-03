
binaryList = []
with open("AdventOfCodePython\PuzzleInputs\day3.txt") as f:
    binaryList = f.readlines()

# part 1
gamma = 0
binarySize = len(binaryList[0])-1
for i in range(binarySize):
    zeroTotal = 0
    oneTotal = 0
    for binaries in binaryList:
        if(int(binaries[i]) == 0):
            zeroTotal += 1
        else:
            oneTotal += 1
    if( oneTotal > zeroTotal):
        print ((2 ** (binarySize-i-1)))
        gamma += (2 ** (binarySize-i-1))
epsilon = (2 ** binarySize) - gamma-1

print(epsilon)
print(gamma)
print("total {}".format(gamma*epsilon))

# part 2
gamma = 0
binarySize = len(binaryList[0])-1
binaryList2 = binaryList

zeroPos = []
onePos = []
for i in range(binarySize):
    zeroTotal = 0
    oneTotal = 0
    for binaries in binaryList:
        if(int(binaries[i]) == 0):
            zeroTotal += 1
            zeroPos.append(binaries)
        else:
            oneTotal += 1
            onePos.append(binaries)
    if( oneTotal > zeroTotal):
        print ((2 ** (binarySize-i-1)))
        gamma += (2 ** (binarySize-i-1))
        for pos in zeroPos:
            binaryList.remove(pos)
    else:
        for pos in onePos:
            binaryList.remove(pos)
epsilon = (2 ** binarySize) - gamma-1

print(epsilon)
print(gamma)
print("total {}".format(gamma*epsilon))