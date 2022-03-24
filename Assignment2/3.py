import numpy as np
from copy import deepcopy as dc

q = []
visited = []
    
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
    return q.pop(0)

def compare(s, g):

    if np.all(s==g) :
        return 1
    else:
        return 0

def findPos(s):
    for i in range(len(s)):
        for j in range(len(s[1])):
            if s[i][j] == -1:
                return [i,j]

def up(s, pos):
    s1 = dc(s)
    if pos[0] == 0:
        return s1
    else:
        line()
        s1[pos[0]-1,pos[1]], s1[pos[0],pos[1]] = s1[pos[0],pos[1]], s1[pos[0]-1,pos[1]]     
        print(s1)
        return s1

def down(s, pos):
    s1 = dc(s)
    if pos[0] == len(s1)-1:
        
        return s1
    else:
        line()
        s1[pos[0]+1,pos[1]], s1[pos[0],pos[1]] = s1[pos[0],pos[1]], s1[pos[0]+1,pos[1]]
        print(s1)
        return s1

def left(s, pos):
    s1 = dc(s)
    if pos[1] == 0:
        return s1
    else:
        line()
        s1[pos[0],pos[1]-1], s1[pos[0],pos[1]] = s1[pos[0],pos[1]], s1[pos[0],pos[1]-1]
        print(s1)
        return s1

def right(s, pos):
    s1 = dc(s)
    if pos[1] == 2:
        return s1
    else:
        line()
        s1[pos[0],pos[1]+1], s1[pos[0],pos[1]] = s1[pos[0],pos[1]], s1[pos[0],pos[1]+1]
        print(s1)
        return s1

def main():
    s0 = np.array([[1,2,3],[8,-1,4],[7,6,5]])
    g = np.array([[2,8,1],[-1,4,3],[7,6,5]])
    curr_state = dc(s0)
    print(curr_state)

    while 1:

        pos = findPos(curr_state)
        
        s1 = up(curr_state, pos)
        if not compare(s1, g):
            enqueue(s1)
        else: break
        s1 = down(curr_state, pos)
        if not compare(s1, g):
            enqueue(s1)
        else: break        
        s1 = left(curr_state, pos)
        if not compare(s1, g):
            enqueue(s1)
        else: break        
        s1 = right(curr_state, pos)
        if not compare(s1, g):
            enqueue(s1)
        else: break
        visited.append(curr_state)
        curr_state = dequeue()
        line()

    print("found, Visited: ", len(visited))
    
if __name__ == '__main__':
    main()