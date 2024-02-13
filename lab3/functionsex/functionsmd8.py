def uniquelist(lst):
    unique = []
    
    for lst in lst:
        if lst in unique:
            continue
        else:
            unique.append(lst)
    print(unique)
lst = [1,0,0,0,5,5,6,7,8]
uniquelist(lst)