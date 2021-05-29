# 2pts
# ask user for input
# put the input into the variable
# slip the crap out of it
# ask if input backward is input forward
# return

userWord = input('What word do you want to check for?')

palindrome = userWord [ : : -1]

if palindrome == userWord:
    print('obviously this is a palindrome')
else: 
    print('this is obviously not a palindrome')
