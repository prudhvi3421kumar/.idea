# % operator for printing integer
age=34
print("my age is %d years" %age)
major="Years"
minor="Months"
print("My age is %d %s, %d %s"%(age,major,6,minor))
print("PI is approximately %60.50f"%(22/7))

meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
print(meal2)
print(meal1)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])

flower = "blue violet"
print('blue' in flower)

flower = "rose"
colour = "red"

print("The {0} is {1}".format(flower,colour))