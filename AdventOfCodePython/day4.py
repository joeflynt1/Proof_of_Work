from collections import deque
import re

bingoNumbers = []
bingoCards = []


def readFile():
    f = open("AdventOfCodePython\PuzzleInputs\day4.txt", "r")
    i = 1
    bingoCard = []
    # List of bingoCard
    bingoCards =[]
    bingoCardRow = []

    readBingoNums = False
    for x in f:
        if(x.__contains__(",")):
            for num in re.findall("[0-9]+", x):
                bingoNumbers.append(num)
            continue
        # Check to see if it is a digit or just the newline character
        if(re.search("[0-9]", x) == None and re.search("\n", x) != "\n"):
            if len( bingoCard ) == 0:
                continue
            bingoCards.append(bingoCard)
            bingoCard = []
            continue
        # Regex that grabs numbers and puts them into a List
        bingoCardRow = re.findall("[0-9]+" , x)
        bingoCard.append(bingoCardRow)
    # Append last bingoCard to bingoCards
    bingoCards.append(bingoCard)
    # Print out bingoCards to make sure it is correctly reading the file
    for card in bingoCards:
        #print ("New Card")
        #print(card)
        return bingoCards
            
# go through list bingoCards with
# bingo numbers. if a card 
# contains the bingo number
# replace that number with 
# -1. if there is a whole
# row or column of -1s then
# that card is the winning card
# check for the winning card at 
# the end of each iteration
def start(bingoCards, bingoNumbers):
    cardTotal = len(bingoCards)
    winCardTotal = []
    for x in bingoNumbers:
        # reversed is needed for pt 2. This allows it to remove the card
        # and not have to worry about skipping the skipping next iterator 
        # in the process
        for card in reversed(bingoCards):
            for row in card:
                for num in row:
                    # if num is equal to x put a "chip" (-1) on it
                    if num == x:
                        xIndex = row.index(x)
                        row[xIndex] = -1
                        if hasAwinner(card, row, xIndex ) == True:
                            # if the card has one remove it
                            bingoCards.remove(card)
                            # once their is no cards remaining in bingoCards
                            # the most recent card removed is the last winner
                            # so performing necessary calculations
                            if len(bingoCards) == 0:
                                xIndex = bingoNumbers[bingoNumbers.index(x)-1]
                                print(card)
                                return calculateScore(card, x)
    return 0 # No last winner, but this should not occur

def hasAwinner(card, row, xIndex):
    # search through the rows to see 
    # if that rule for winning is hit
    for x in row:
        if x != -1:
            break
    else:
        return True
    # search through columns to see 
    # if that rule for winning is hit
    for cardRow in card:
        if cardRow[xIndex] != -1:
            break
    else:
        return True
    # There has not been a winner
    return False 

def calculateScore(card, bingoNum):
    total = 0
    for row in card:
        for x in row:
            if x != -1:
                total += int(x) 
    return total*int(bingoNum)

def main():
    #print (start(readFile(), bingoNumbers))
    #if start(readFile(), bingoNumbers) > 1:
        print("there is a winner")
        print(start(readFile(), bingoNumbers))
    
main()