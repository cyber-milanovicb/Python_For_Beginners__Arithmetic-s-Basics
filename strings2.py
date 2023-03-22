phrase = "Norwegian Blue"
#                   1
#         012345678901234


print(phrase)

print(phrase[3])
print(phrase[4])
print(phrase[9])

print(phrase[3])
print(phrase[6])
print(phrase[8])

print()

print(phrase[3])
print(phrase[4])
print(phrase[9])
print(phrase[3])
print(phrase[6])
print(phrase[8])

print()
print(phrase[-11])
print(phrase[-10])

print()

print(phrase[-11])
print(phrase[-8])
print(phrase[-6])

print()

# This is also way to do it, as there are in total 14 index numbers, so just using those minus total of charachters and:
print(phrase[3 - 14])
print(phrase[4 - 14])

print(phrase[9 - 14])
print(phrase[3 - 14])
print(phrase[6 - 14])
print(phrase[8 - 14])

#                    1
phrase = "Norwegian     Blue"
#         0123456789 0  1234

print(phrase[0:6]) # = Norweg
print(phrase[3:5]) # = weg

# now with these - you will get same result with both examples:
print(phrase[0:9])
print(phrase[:9])   # assumption at Python that 1st index nmber is 0.
