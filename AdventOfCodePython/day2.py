import re

def direction(dVal, distance):
    if( dVal == "backward" or dVal == "up" ):
        return distance * -1
    return distance

#part 1
movements = []
with open('AdventOfCodePython\PuzzleInputs\day2.txt') as f:
    movements = f.readlines()

horizontal = 0
elevation = 0
for movement in movements:
    info = movement.split(" ")
    direction = info[0]
    distance = int(info[1])
    if(direction == "forward"):
        horizontal += distance
    elif ( direction == "up"):
        elevation -= distance
    else:
        elevation += distance
print(horizontal*elevation)

#part 2
horizontal = 0
elevation = 0
aim = 0
for movement in movements:
    info = movement.split(" ")
    direction = info[0]
    distance = int(info[1])
    if(direction == "forward"):
        horizontal += distance
        elevation += aim*distance
    elif ( direction == "up"):
        aim -= distance
    else:
        aim += distance
        
print(horizontal*elevation)






