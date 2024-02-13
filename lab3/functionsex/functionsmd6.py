def spygame(nums):
    check_str = ""
    for num in nums:
        if num == 0 or num == 7:
            check_str += str(num)
    return "007" in check_str
print(spygame([1,2,4,0,0,7,5])) #--> True
print(spygame([1,0,2,4,0,5,7])) #--> True
print(spygame([1,7,2,0,4,5,0])) #--> False

    



    