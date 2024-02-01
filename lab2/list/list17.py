newlist = [x for x in range(10)]
print(newlist)

newlist1 = [x for x in range(10) if x < 5]
print(newlist1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x.upper() for x in fruits]
print(newlist2)

newlist3 = ['Nikitka' for x in fruits]
print(newlist3)

newlist4 = [x if x != "banana" else "orange" for x in fruits]
print(newlist4)