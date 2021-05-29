# CodeWars 2021 Problem 8 | 3-6-21
# Emily Broad and Sierra Janson

# unpack ints
# [0] = wall height
# [1] = punch height
# [2] = anger level (every 10 means +1 distance from original wall)
# for wall height - punch height print # with breaks 
# then . for each anger level 
# then punch height num of # no breaks

my_File = open("CodeWars\prob8.txt",'r')
data = []
for line in my_File:
    data = line.split()
# print(data)

wall_Height = data[0]
punch_Height = data[1]
how_Angry = data[2]
original_Wall = int(punch_Height) - 1
crashed_Wall  = int(wall_Height) - int(punch_Height) + 1
punch_Distance = int(how_Angry) / 10
# print(wall_Height, punch_Height, how_Angry)

if int(punch_Height) > int(wall_Height):
    for h in range(0, int(wall_Height)):
        print('#')
else:
    if int(punch_Height) == 0:
        for i in range(0, int(wall_Height)):
            print('#')
    else:        
        for j in range(1, original_Wall + 1):
            if j != original_Wall:
                print('#')
            else:
                print('#', end = '')
        for i in range(0, int(punch_Distance)):
            print('.', end = '')
        for i in range(0, int(crashed_Wall)):
            print('#', end = '')
