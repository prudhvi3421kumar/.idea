for i in range(1,13):
    print("No.{0} is Squared is {1} and cubed is {2}".format(i,i**2,i**3))
# now we do the formatting to right alignment
for i in range(2,14):
    print("No.{0:2} is Squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))

# now we do the formatting to left alignment
for i in range(2,14):
    print("No.{0:2} is Squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3))

#Caret symbol for center alignment
for i in range(2,14):
    print("No.{0:2} is Squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))

print()
# floting point precision
print(" The Pi value:{0:12}".format(22/7))
print(" The Pi value:{0:12f}".format(22/7))
print(" The Pi value:{0:12.50f}".format(22/7))
print(" The Pi value:{0:52.50f}".format(22/7))
print(" The Pi value:{0:62.50f}".format(22/7))
print(" The Pi value:{0:72.50f}".format(22/7))
print(" The Pi value:{0:<72.50f}".format(22/7))
print(" The Pi value:{0:<72.54f}".format(22/7))
# we cann use field width
for i in range(2,14):
    print("No.{} is Squared is {} and cubed is {:4}".format(i,i**2,i**3))