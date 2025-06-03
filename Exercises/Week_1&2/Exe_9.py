year = int(input("Enter a year"))

# To print a variable in a string statement, we use several methods.

# First Method : Place Holder

st = str("The year is %s" %year)
print (st)

st = str("The year is %s" % (year))
print (st)

st = str(f"The year is {year}")
print (st)

st = str("The year is {}".format(year))
print (st)