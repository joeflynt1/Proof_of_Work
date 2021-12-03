depths = []
with open('AdventOfCodePython\PuzzleInputs\day1.txt') as f:
    depths = f.readlines()

prev = int(depths[0])
total = 0
for current in depths:
    if (int(current) > int(prev)):
        total= total + 1
    prev = current
print("total increases {}".format(total))

total = 0
totalLines = len(depths)
for i in range(totalLines):
    if(i+4<=totalLines):
        if((int(depths[i])+int(depths[i+1])+int(depths[i+2]))<(int(depths[i+1])+int(depths[i+2])+int(depths[i+3]))):
            total += 1
    else:
        break
print("total increases {}".format(total))