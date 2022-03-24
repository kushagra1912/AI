l1 = [1,2,3,4,5,6]
l2 = [5,6,7,8,9,10,11,12,13]

com = []

for i in l1:
    if i in l2:
        com.append(i)

print("Common Elements: {}".format(com))