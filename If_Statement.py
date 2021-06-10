name=input("Please tell me your name: ")
age=int(input("what is your age? {}:".format(name)))
print("name is "+name+" and age is "f"{age} years old")
#print(type(age))
# if age>=18:
#     print("You are old enough to vote, Thank you")
#     print("Please cast your vote")
# else:
#     print("Please come back in {} years".format(18-age))
if age<18:
    print("Please come back in {} years".format(18-age))
elif age==900:
    print(" you have given wrong age")
    exit
else:
    print("You are old enough to vote, Thank you")
    print("Please put an X in the box")


