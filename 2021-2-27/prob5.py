# CodeWars 2021 Problem 5 | 2-27-21
# Emily Broad and Sierra Janson

# Import data from file
# Convince compiler that A * (B + C) == A * B + A * C
# Print work to convice the people that the compiler is convinced

file = open("2-27-2021\prob5.txt", "r")
input_data = []
for line in file:
    input_data.append(line.strip())
    
A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])

print(f"{A} * ({B} + {C}) == {A} * {B} + {A} * {C}")
print(f"{A} * {B + C} == {A * B} + {A * C}")
print(f"{A * (B + C)} == {(A * B) + (A*C)}")
