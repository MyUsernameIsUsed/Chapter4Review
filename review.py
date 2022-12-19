#Chapter 4 review 
# if your string length is 9 charcters long count of charcters goes from 0 -8
text = "Good Morning!" #13 charcters - count 0 - 12
print(len(text))

# subscript operator []
# text[0] - G
# text[7] - r
# check length: len(text) Length function
# Last Character
print(text[-1])
# count backwards
print(text[-3]) # n
print(text[-13]) # G

print("Slicing Strings:")
name = "myfile.txt"
# Entire string
name[0:] # Print entire string 
# First Character 
print(name[0:1]) # prints character 1 or 'm'
# Entire string Example 2:
print(name[:len(name)]) # entire string 
# First 2 characters
print(name[0:2])
# First 5 characters
print(name[0:5])
#Last 3 characters
print(name[-3:])

#4-1d Testing for a substring with the in Operator
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)


print()
print("Caesar cipher:")
plainText = "Welcome to Software Development"
key = 5
code = ""
for ch in plainText:
    ordVal = ord(ch)
    cipherVal = ordVal + key
    if cipherVal > ord('z'):
        cipherVal = ord('a') + key - (ord('z') - ordVal + 1)
    code += chr(cipherVal)
print(code)

print()
print("Decrypt Caesar Cipher")
# code
# key
plainText = ""
for ch in code:
    ordVal = ord(ch)
    cipherVal = ordVal - key
    if cipherVal < ord('z'):
        # cipherVal = ord('a') - (key - (ord("z") - ordVal - 1))
        #             #       1.  + 5.         26 -  3   +1
        #             #           6-24
        #             #             -18
        cipherVal += 26
    plainText += chr(cipherVal)
print(code)
print(plainText)

print()
print("Binary to Decimal")
bitString = input("Enter a string of bits:")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
    print("The integer value is: ", decimal)

print()
print("Decimal to Binary")
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else: 
    print("Quotient Remaineder Binary")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder, bitString))
    print("The binaryy representation is:", bitString)