down = int(input())
up = int(input())

prime = []

for i in range(down, up + 1):
    if i <= 1:
        continue
    else:
        flag = 0
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                flag = 1
        if flag == 0 or i == 2:
            prime.append(i)

print("No. of prime numbers:{}\nList of prime numbers: {}".format(len(prime),prime))