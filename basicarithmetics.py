a = 15
b = 3

print(a + b)  # 18
print(a - b)  # 12
print(a * b)  # 45
print(a / b)  # 5.0
print(a // b)  # 5 integer division, number is rounded down minus infinity
print(a % b)  # 0 module, the "reminder" after integer division


print()
for i in range(1, 4):
    print(i)

# You cannot do following

""" for i in rage(1, a/b):
    print(i) """

# what you can do is:

for i in range(1, a // b):
    print(i)

# can't use float

