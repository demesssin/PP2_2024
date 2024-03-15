def all_true(t):
    return all(t)

my_tuple = (True, True, True)
print(all_true(my_tuple)) 

my_tuple = (True, False, True)
print(all_true(my_tuple)) 
