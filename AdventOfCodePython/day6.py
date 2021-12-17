# brute force way that works for pt 1 but causes memory error


def parseFile():
    f = open("AdventOfCodePython\PuzzleInputs\day6.txt")
    fishDays = []
    for line in f:
        for fishDay in line.split(","):
            fishDays.append(int(fishDay))
    return fishDays

def start(fishDays):
    for i in range(len(fishDays)-1, -1, -1) :
        if fishDays[i] == 0:
            fishDays.append(8)
            fishDays[i] = 7
        fishDays[i] -= 1
    return fishDays

    # This code is commented out since it will cause the memory error 
    # otherwise
#currentFishDays = 0
#schoolList = start(parseFile())
#for i in range(255) :
#    schoolList = start(schoolList)
#print("Total Fish {}".format(longint(len(schoolList))))


# Begin part 2 stuff

# Map to hold all of the fish counts based on current day
pt2fishDays = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }

# function to parse a file, returns as a fish days Dictionary
def pt2ParseFile():
    f = open("AdventOfCodePython\PuzzleInputs\day6.txt")
    for line in f:
        for fishDay in line.split(","):
            pt2fishDays[int(fishDay)]+=1
    return pt2fishDays

def pt2Start(fishDays):
    # Record current zeroCount value
    zeroCount = fishDays[0]
    fishDays[0] = 0
    # loop through the map, Move the fish up 1 day in their breeding cycle
    for i in range(1,len(fishDays),1) :
        fishDays[i-1] = fishDays[i]
    # if the fish is on its breading day create a birth fishes then reset it to
    # current fishes to its day 6
    fishDays[6] += zeroCount
    fishDays[8] = zeroCount
    return fishDays

# Cycle through specified number of days. 
# in this case 256. If this were a project rather than one file it would also be a good idea to 
# potentially use an enumeration here
schoolDict = pt2ParseFile()
for i in range(256) :
    schoolDict = pt2Start(schoolDict)

totalFish = 0
# Count up the total number of fish
for i in range(len(schoolDict)):
    totalFish += schoolDict[i]
# Print out the total which is the final answer
print (totalFish)