import numpy as np
from copy import deepcopy as dc

q = []
visited = []


def dist(s,g):
    d = 0
    for i in range(len(s)):
        for j in range(len(s)):
            coorS = [i,j]
            coorG = findPos(g,s[i][j])
            d += (coorS[0]-coorG[0])**2 + (coorS[1]-coorG[1])**2
    return d**0.5

def line():
    print('-'*50)

def enqueue(s):
    flag = 0
    for i in visited:
        if compare(i, s):
            flag = 1
            break
    if not flag:
        q.append(s)

def dequeue():
    q.sort()
    a = q.pop(0)
    return a[1]

def compare(s, g):

    if np.all(s==g) :
        return 1
    else:
        return 0

def findPos(s,val):
    for i in range(len(s)):
        for j in range(len(s[1])):
            if s[i][j] == val:
                return [i,j]

def up(s, pos):
    s1 = dc(s)
    if pos[0] == 0:
        return s1
    else:
        s1[pos[0]-1][pos[1]], s1[pos[0]][pos[1]] = s1[pos[0]][pos[1]], s1[pos[0]-1][pos[1]]             
        return s1

def down(s, pos):
    s1 = dc(s)
    if pos[0] == len(s1)-1:
        
        return s1
    else:
        s1[pos[0]+1][pos[1]], s1[pos[0]][pos[1]] = s1[pos[0]][pos[1]], s1[pos[0]+1][pos[1]]        
        return s1

def left(s, pos):
    s1 = dc(s)
    if pos[1] == 0:
        return s1
    else:
        s1[pos[0]][pos[1]-1], s1[pos[0]][pos[1]] = s1[pos[0]][pos[1]], s1[pos[0]][pos[1]-1]        
        return s1

def right(s, pos):
    s1 = dc(s)
    if pos[1] == 2:
        return s1
    else:
        s1[pos[0]][pos[1]+1], s1[pos[0]][pos[1]] = s1[pos[0]][pos[1]], s1[pos[0]][pos[1]+1]        
        return s1

def main():
    g = [[1,2,3],[8,-1,4],[7,6,5]]
    s0 = [[2,-1,3],[1,8,4],[7,6,5]]
    curr_state = dc(s0)
    print(curr_state)
    while 1:
        pos = findPos(curr_state,-1)
        s1 = up(curr_state, pos)
        d = dist(s1,g)
        if not compare(s1, g):
            line()
            print(s1)
            enqueue([d,s1])
        else: break
        s1 = down(curr_state, pos)
        d = dist(s1,g)
        if not compare(s1, g):
            line()
            print(s1)
            enqueue([d,s1])
        else: break        
        s1 = left(curr_state, pos)
        d = dist(s1,g)
        if not compare(s1, g):
            line()
            print(s1)
            enqueue([d,s1])
        else: break        
        s1 = right(curr_state, pos)
        d = dist(s1,g)
        if not compare(s1, g):
            line()
            print(s1)
            enqueue([d,s1])
        else: break
        d = dist(curr_state,g)
        visited.append([d,curr_state])
        curr_state = dequeue()
    print("found")
    
if __name__ == '__main__':
    main()
