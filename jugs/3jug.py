import numpy as np
from copy import deepcopy as dc

q = []
visited = []
maxCap = [12,8,5]

def line(currCap = []):
    print('-'*50)
    print(currCap)

def enqueue(s):
    flag = 0
    for i in visited:
        if qCompare(i, s):
            flag = 1
            break
    for i in q:
        if qCompare(i, s):
            flag = 1
            break
    if not flag:
        q.append(s)

def dequeue():
    return q.pop(0)

def qCompare(s, g):
    if np.all(s==g) :
        return 1
    else:
        return 0

def compare(newCap):
    if newCap[0] == 6 :
        return 1
    else:
        return 0

def transfer(currCap, no1, no2):
    currCap = dc(currCap)
    if no1 == 1 and currCap[0] < maxCap[0]:
        if no2 == 2 and currCap[1] != 0:
            while(currCap[0] < maxCap[0] and currCap[1] > 0):
                currCap[0]+= 1 
                currCap[1]-= 1 
            
        if no2 == 3 and currCap[2] != 0:
            while(currCap[0] < maxCap[0] and currCap[2] > 0):
                currCap[0]+= 1 
                currCap[2]-= 1        

    if no1 == 2 and currCap[1] < maxCap[1]:
        if no2 == 1 and currCap[0] != 0:
            while(currCap[1] < maxCap[1] and currCap[0] > 0):
                currCap[1]+= 1 
                currCap[0]-= 1
        if no2 == 3 and currCap[2] != 0:
            while(currCap[1] < maxCap[1] and currCap[2] > 0):
                currCap[1]+= 1 
                currCap[2]-= 1

    if no1 == 3 and currCap[2] < maxCap[2]:
        if no2 == 1 and currCap[0] != 0:
            while(currCap[2] < maxCap[2] and currCap[0] > 0):
                currCap[2]+= 1 
                currCap[0]-= 1
        if no2 == 2 and currCap[1] != 0:
            while(currCap[2] < maxCap[2] and currCap[1] > 0):
                currCap[2]+= 1 
                currCap[1]-= 1
    line(currCap)
    return currCap

def main():
    j = [12,0,0]
    g = [2,0]
    currCap = dc(j)
    while(1):
                #Jug 1 Transfers
        newCap = transfer(currCap,2,1)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,3,1)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,3,1)
        newCap = transfer(newCap,2,1)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,2,1)
        newCap = transfer(newCap,3,1)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        #Jug 2 Transfers
        newCap = transfer(currCap,1,2)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,3,2)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,1,2)
        newCap = transfer(newCap,3,2)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,3,2)
        newCap = transfer(newCap,1,2)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        #Jug 3 Transfers
        newCap = transfer(currCap,1,3)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,2,3)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,1,3)
        newCap = transfer(newCap,2,3)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        newCap = transfer(currCap,2,3)
        newCap = transfer(newCap,1,3)
        if not compare(newCap):
            enqueue(newCap)
        else: break
        visited.append(currCap)
        currCap = dequeue()
    print("Found")

if __name__ == '__main__':
    main()