# CodeWars 2021 Problem 6 | 3-6-21
# Emily Broad and Sierra Janson

# simple cipher, prob use dictionary

# PLAINTEXT ABCDEFGHIJKLMNOPQRSTUVWXYZ
# CIPHERTEXT FGHIJKLMNOPQRSTUVWXYZABCDE

my_File = open("CodeWars\prob6.txt",'r')
input = []
for line in my_File:
    input.append(line.strip())

must_Decipher = input[1]
# print(must_Decipher)

decode = {
    'F':'A',
    'G':'B',
    'H':'C',
    'I':'D',
    'J':'E',
    'K':'F',
    'L':'G',
    'M':'H',
    'N':'I',
    'O':'J',
    'P':'K',
    'Q':'L',
    'R':'M',
    'S':'N',
    'T':'O',
    'U':'P',
    'V':'Q',
    'W':'R',
    'X':'S',
    'Y':'T',
    'Z':'U',
    'A':'V',
    'B':'W',
    'C':'X',
    'D':'Y',
    'E':'Z',
    ' ':' '
}

for i in must_Decipher:
    print(i.replace(i, decode[i]), end = '')
