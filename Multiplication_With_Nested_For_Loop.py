for i in range(1,13):
    for j in range(1,13):
        print("{0:2} times {1:3} is {2:4}".format(i,j,i*j))
    print("----------------------------")

for i in range(1,13):
    for j in range(1,13):
        print("{0:2} times {1:3} is {2:4}".format(j,i,i*j))
    print("----------------------------")