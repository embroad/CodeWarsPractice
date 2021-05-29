# packs of 6, 11, or 13 peppers
# take peppers and find the most economic way to pack
# input must be an int and < 1000
# take input and output how many of each pack
# mostly division

import sys

numPeppers = input('How many peppers are you shipping? ')

if '.' in numPeppers:
    input('Please input an integer: ')
    numPeppers = input()
else:
    numPeppers = int(numPeppers)
    if numPeppers > 1000:
        input('Please input an integer: ')
        numPeppers = input()

# so we want the least number of packs
# probably won't divide evenly
# start by looking for how many times 13 goes into it and make sure the remainder is bigger than 6
# then make sure when you divide by 11, the remainder is bigger than 6
# then when you divide by 6, the remainder has to be 0

num6 = []
num11 = []
num13 = []

if (numPeppers % 13) < 6:
    if (numPeppers % 11) < 6:
        if (numPeppers % 6) != 0:
            print("This can't be packed :(")

#if (numPeppers % 13) > 6:
#       if (numPeppers % 6) == 0:
