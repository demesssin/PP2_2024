thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#tuples allow duplicates

thistuple = ("apple",) # To create a tuple with only one item, 
print(type(thistuple)) # you have to add a comma after the item, 
                       # otherwise Python will not recognize it as a tuple.
                       
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)