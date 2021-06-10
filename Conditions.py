age=int(input("Please enter your age: "))
#if age>=16 and age<=65:
if 16<=age<=65:
    print("Have a good day at work")
else:
    print("enjouy your free time")

print("*-"*50)

if age<16 or age>65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")