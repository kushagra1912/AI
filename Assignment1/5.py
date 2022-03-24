up = int(input())
down = int(input())

leap = []

for i in range(down, up + 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        leap.append(i)

print("ist of leap years: {}".format(leap))
