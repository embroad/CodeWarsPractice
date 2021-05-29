# CodeWars 2021 Problem 3 | 2-27-21
# Emily Broad and Sierra Janson

file = open("2-27-2021\prob3.txt", "r")
input_data = []
for line in file:
    input_data.append(line.strip())

conversions = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : "five",
    '6' : "six",
    '7' : "seven",
    '8' : "eight",
    '9' : "nine",
    '10' : "ten",
}

for index in input_data:
    index = 0
    print(f"Number {conversions[(input_data[index])]} is alive!")
