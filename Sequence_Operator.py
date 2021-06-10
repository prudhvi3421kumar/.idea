string1="he's"
string2="probably "
string3="pining "
string4="for the "
string5="fjords"
print(string1+string2+string3+string4+string5)
print("he's" "probably " "pining " "for the " "fjords" )
# we can multiply strings and concatenate
print("Hello "*5)
print("Hello "*(5+4))
print("Hello "*5+"4")

#“ in” operator evaluates to True if the first thing exists in the second

today="Friday"
print("day" in today)   # true
print("Fri" in today)   # true
print("myself" in today)# false
print("parrot" in "fjord") #false

