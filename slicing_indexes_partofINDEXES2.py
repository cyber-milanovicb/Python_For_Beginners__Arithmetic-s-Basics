#                  1
#         012345678901234
phrase = "Norwegian Blue"

print(phrase[0:6:2]) #Nre
print(phrase[0:6:3]) #Nw

number = "9,223;327:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])