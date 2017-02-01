'''DynamicPrograming_RNA_Folding.py'''
# Kyle Desmond Patterson
# January 31, 2017

import numpy as np

def isComplement(base1, base2):
    '''Returns boolean indicating if 2 RNA bases are complementary.'''
    if base1=="A" and base2=="U":
        return True
    elif base1=="U" and base2=="A":
        return True
    elif base1=="C" and base2=="G":
        return True
    elif base1=="G" and base2=="C":
        return True
    if base1=="G" and base2=="U":
        return True
    elif base1=="U" and base2=="G":
        return True
    else:
        return False

def myMax(myList):
    '''
    Takes in a list of tuples with a score value as their
    first element and returns the tuple with the highest score.
    Ties are broken by tuples of higher indicies.
    '''
    maxTuple = (0,)
    for myTuple in myList:
        if myTuple[0] >= maxTuple[0]:
            maxTuple = myTuple
    return maxTuple

def fillDP(start, end):
    '''Fills cells in a given diagonal in DP table.'''
    
    global DP # declare we want to use the global DP table
    global RNA # declare we want to use the global RNA string

    (row, col) = start # unpack start coordinates
    (row2, col2) = end # unpack end coordinates

    diff = row - col

    for myCol in range(col, col2 + 1): # iterate through columns
        myRow = myCol + diff # get row from current column and initial difference

        # find bases to which indicies correspond
        baseC = RNA[myCol]
        baseR = RNA[myRow]

        # consider use base option
        if isComplement(baseR, baseC):
            score = 1.0
        else:
            score = 0.0
        useIt = score + DP[myRow + 1][myCol - 1]

        # consider lose base option
        loseIt = DP[row + 1][col]

        # set value in DP table to max of options
        DP[myRow][myCol] = max(useIt, loseIt)

def foldDP(RNAstring):
    '''
    Using dynamic programming, returns the maximum number of possible
    matches in an RNA string.
    '''
    
    global DP # declare we want to use the global DP table
    global RNA # declare we want to use the global RNA string

    length = len(RNAstring)
    DP = np.zeros((length, length), dtype = float) # make empty 2D DP table
    RNA = RNAstring

    numDiag = length - 1 # num diag from one above middle diag to top right corner

    for diag in range(1, length): # iterate through diagonals
        fillDP((0, diag), (numDiag - diag, numDiag)) # fill in values for each diagonal

    return DP[0, numDiag]

def getStructDP():
    ''''''
    pass