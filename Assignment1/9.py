D = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}

D.update({6:"Six"})
print(D)
D.pop(2)
print(D)

if 6 in D:
    print("6 is in D")
else:
    print("6 is not in D")
print(len(D))
sum = ""
for i in D.values():
    sum += i
print(sum)

