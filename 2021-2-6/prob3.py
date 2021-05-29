# 3pts
# mport inputs
# split up the inputs
# print the dumb thing

import sys
lines = []
file = open("prob3.txt", "r")

for line in file:
    lines.append(int(line))

# print(lines)

for i in lines:
    for n in range(0,4):
        for n in range(0,i):
            print( ('#'*i +  '.'*i)*8 )
        for n in range(0,i):
            print( ('.'*i +  '#'*i)*8 )
