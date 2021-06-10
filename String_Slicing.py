#       012345678
parrot="Norwegian Blue"
print(parrot)
#slicing is done with start, stop and step values
print(parrot[0:6])# Norweg
print(parrot[3:5])# we
print(parrot[0:9])# Norwegian
print(parrot[:9])
print(parrot[10:])
print(parrot[10:14])
print(parrot[:6])
print(parrot[6:])

print(parrot[:6]+parrot[6:])

print(parrot[:])
# negative indexing
print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[-14:-8])
print(parrot[0:6:2])
print(parrot[0:6:3])

number="9,223,372,036,854,775,807"
print(number[1::4])# slicing happens for each 4th place
number1="9,223;372:036 854,775;807"
seperators=number1[1::4]
print(seperators)
values="".join(char if char not in seperators else " " for char in number1).split()
print([int(val) for val in values])