def daryn(x):
    return x % 2 == 1

sandar = [1,2,3,4,5,6,7,8,9,10]

jup_sandar = filter(daryn, sandar)

jup_sandar_jiyny = list(jup_sandar)

print(jup_sandar_jiyny)