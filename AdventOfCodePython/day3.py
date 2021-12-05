
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
        if(int(binaries[i]) == 0): # check for most common bit and increment accordingly
            zeroTotal += 1 
        else:
            oneTotal += 1
    if( oneTotal > zeroTotal): # if the most common bit is a 1 then add the value to the gamma
        gamma += (2 ** (binarySize-i-1))
epsilon = (2 ** binarySize) - gamma-1 # since this is binary you only have to do the opposite of the current value


print(gamma) #most common
print(epsilon) #least common
print("total {}".format(gamma*epsilon)) 


# part 2
binarySize = len(binaryList[0])-1
binaryList2 = []
for binary in binaryList:
    binaryList2.append(binary)
    


for i in range(binarySize):
    zeroTotal = 0
    oneTotal = 0
    zeroPos = []
    onePos = []
    for binaries in binaryList:
        if( int(binaries[i] ) == 0):
            zeroTotal += 1
            zeroPos.append(binaries)
        else:
            oneTotal += 1
            onePos.append(binaries)
    # Computes OGR 
    if( oneTotal >= zeroTotal ): 
        for pos in zeroPos: 
            binaryList.remove(pos)     
    else:
        for pos in onePos:  
            binaryList.remove(pos)

    print("iteration {}".format(i))
    print("OGR")


    for binary in binaryList:
        print("{}".format(binary))
    zeroTotal = 0
    oneTotal = 0
    zeroPos = []
    onePos = []
    for binaries in binaryList2:
        if( int(binaries[i] ) == 0):
            zeroTotal += 1
            zeroPos.append(binaries)
        else:
            oneTotal += 1
            onePos.append(binaries)
    if( oneTotal >= zeroTotal ): 
        for pos in onePos:  # CO2
            binaryList2.remove(pos)        
    else:
        for pos in zeroPos: # CO2
            binaryList2.remove(pos)
    if( len(binaryList2) == 1):
        print("CO2")
        for binary in binaryList2:
            print("{}".format(binary))
    
