list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# OTHER METHOD

list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]

for x in list5:
  list4.append(x)

print(list4)

# OTHER METHOD

list6 = ["a", "b" , "c"]
list7 = [1, 2, 3]

list6.extend(list7)
print(list6)