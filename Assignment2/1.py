import numpy as np
from copy import deepcopy as dc

q = []
visited = []
maxCap = [4,3]

def line(currCap):
    print('-'*50)
    print(currCap)

def enqueue(s):
    flag = 0
    for i in visited:
        if compare(i, s):
            flag = 1
            break
    for i in q:
        if compare(i, s):
            flag = 1
            break
    if not flag:
        q.append(s)

def dequeue():
    return q.pop(0)

def compare(s, g):
    if np.all(s==g) :
        return 1
    else:
        return 0

def fill(currCap, no):
    currCap = dc(currCap)
    if no == 1:
        currCap[0] = 4
    if no == 2:
        currCap[1] = 3
    line(currCap)
    return currCap

def empty(currCap, no):
    currCap = dc(currCap)
    if no == 1:
        currCap[0] = 0
    if no == 2:
        currCap[1] = 0
    line(currCap)
    return currCap

def transfer(currCap, no):
    currCap = dc(currCap)
    if no == 1:
        diff = currCap[1] - currCap[0]
        if diff > 0 and currCap[0] + diff < maxCap[0] and (currCap[1] - (maxCap[0] - currCap[0])) >= 0:
            currCap[1] = currCap[1] - diff
            currCap[0] = currCap[0] + diff
        elif diff > 0 and currCap[0] + diff >= maxCap[0]:
            fill(currCap, 1)
            currCap[1] = currCap[1] - (maxCap[0] - currCap[0])
            print("here")

    if no == 2:
        diff = currCap[0] - currCap[1]
        if diff > 0 and currCap[1] + diff < maxCap[1] and (currCap[0] - (maxCap[1] - currCap[1])) >= 0:
            currCap[1] = currCap[1] - diff
            currCap[0] = currCap[0] + diff
        elif diff > 0 and currCap[1] + diff >= maxCap[1]:
            fill(currCap, 2)
            currCap[0] = currCap[0] - (maxCap[1] - currCap[1])
    line(currCap)
    return currCap

def main():
    j = [0,0]
    g = [2,0]
    currCap = dc(j)
    while(1):
        newCap = fill(currCap, 1)
        if not compare(newCap, g):
            enqueue(newCap)
        else: break
        newCap = fill(currCap, 2)
        if not compare(newCap, g):
            enqueue(newCap)
        newCap = empty(currCap, 1)
        if not compare(newCap, g):
            enqueue(newCap)
        else: break
        newCap = empty(currCap, 2)
        if not compare(newCap, g):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,1)
        if not compare(newCap, g):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,2)
        if not compare(newCap, g):
            enqueue(newCap)
        else: break
        visited.append(currCap)
        currCap = dequeue()
        
    print("Found")




if __name__ == '__main__':
    main()