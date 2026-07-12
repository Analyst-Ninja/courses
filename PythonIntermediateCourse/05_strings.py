# Strings:
# 1. Ordered
# 2. Immutable
# 3. Text Representation

import time

myString = "Hello World"

# myString[0] = "W" # Immuatable --> Can't Change the string however can assign it to different varaible

# print(myString)

# print(myString.startswith('Hello'))
# print(myString.endswith('Hello'))

# print(myString.find('o'))
# It will give the index for character to find in a string
# Or it will return -1 if the character is present

# print(myString.find('pp'))

# print(myString.count('l'))

# print(myString.replace('World','Universe'))
# print(myString.replace('Worlddd - Type','Universe')) # It wont change anything

# newString = 'how are you doing?'

# print(newString.split())

# listOfWords = newString.split()

# string = " ".join(listOfWords)

# print(string)

# print(['a']*3)

# # Joining the Strings
# # 1. bad

# l = ['a']*1000000
# start = time.time()
# myString = ''
# for i in l:
#     myString += i
# end = time.time()
# print(end - start)

# # 2. Good
# start = time.time()
# joinedStr = ''.join(l)
# end = time.time()
# print(end - start)

# Formatting the String

# 1. Way 1 - Using %
var = "Tom"
intNum = 3
floatNum = 3.1456747
print("my string is %s" % var)
print("my string is %d" % intNum)
print("my string is %f" % floatNum)
print("my string is %.2f" % floatNum)

# 2. Way 2 - Using format method
var = "Tom"
intNum = 3
floatNum = 3.1456747
print("My string is {0} {1} {2} {2:.2f}".format(var, intNum, floatNum))

# 3. Way 3 - Using f-string
var = "Tom"
intNum = 3
floatNum = 3.1456747
print(f"My string is {var} {intNum * 2} {floatNum} {round(floatNum,2)}")
