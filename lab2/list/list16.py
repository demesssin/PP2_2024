fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print("SOOOO OOOOOON")

fruits1 = ["guawa", "arbuz", "kiwi", "mindirin", "mybebaby"]

newlist1 = [z for z in fruits1 if "a" in z]

print(newlist1)
print("SOOOO OOOOOON")

newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)