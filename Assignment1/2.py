import random as r

arr1 = []

for i in range(100):
    arr1.append(r.randint(100,900))

odd, even, prime = [], [], []


for i in arr1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    if i <= 1:
        continue
    else:
        flag = 0
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                flag = 1
        if flag == 0 or i == 2:
            prime.append(i)

print("No. of odd numbers:{}\nList of odd numbers: {}\nNo. of even numbers:{}\nList of even numbers: {}\nNo. of prime numbers:{}\nList of prime numbers: {}".format(len(odd),odd,len(even),even,len(prime),prime))