#Using “str” operator to coerce the integer to string do the concatenation
age=33
print("My age is "+str(age)+" Years")
#Using .format() operator
print("My age is {} Years".format(age))
print("There are {0} days in {1},{2},{3},{4},{5},{6},{7}"
      .format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec"
      .format(31))
# it is to show that the {value in side can be palced in any order}
print("Jan:{2},\n Feb:{0},\n Mar:{2},\n Apr:{1},\n May:{2},\n Jun:{1},\n Jul:{2},\n Aug:{2},\n Sep:{1},\n Oct:{2},\n Nov:{1},\n Dec:{2} days"
      .format(28,30,31))

#we can triple quotes
print("""Jan:{2}
Feb:{0}
Mar:{2}
Apr:{1}
May:{2}
Jun:{1}
Jul:{2}
Aug:{2}
Sep:{1}
Oct:{2}
Nov:{1}
Dec:{2} """.format(28,30,31))