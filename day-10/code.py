
dirs = {"|":[(1,0),(-1,0)], "-":[(0,1),(0,-1)], "L":[(1,0),(0,-1)], "J":[(1,0),(0,1)], "7":[(0,1),(-1,0)], "F":[(-1,0),(0,-1)]}

maxX, maxY = 0, 0

def direction(a, b, c):
    diff = (b[0] - a[0], b[1] - a[1])
    d = dirs[c]
    if c in ["|","-"]:
        return diff
    else:
        if diff == d[0]:
            return (-d[1][0], -d[1][1])
        else:
            return (-d[0][0], -d[0][1])

def move (a,dir):
    return (a[0]+ dir[0], a[1]+ dir[1])

dirr = [(1,0),(-1,0),(0,1),(0,-1)]
def leak(a, map, pipes):
    if a in pipes: return
    if a[0] < 0 or a[0] >maxX or a[1] < 0 or a[1] > maxY: return

    pipes.add((a[0],a[1]))
    x = map[a[0]]
    y = x[:a[1]] + 'I' + x[a[1]+1:]
    map[a[0]] = y
    for d in dirr:
        newp = move(a, d)
        leak(newp, map, pipes)


def left(a, map, visited):
    pos = a[0]
    dir = a[1]
    char = map[pos[0]][pos[1]]
    if char == 'S': return
    mvm = 0
    if char == 'F':
        if dir == (0,-1):
            mvm = [(pos[0] + 1, pos[1] + 1)]
        else:
            mvm = [(pos[0], pos[1] - 1), (pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1])]
    elif char == '|':
        if dir == (1,0):
            mvm = [(pos[0], pos[1] + 1)]
        else:
            mvm = [(pos[0], pos[1] - 1)]
    elif char == 'L':
        if dir == (1,0):
            mvm = [(pos[0] - 1, pos[1] + 1)]
        else:
            mvm = [(pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] - 1), (pos[0], pos[1] - 1)]
    elif char == 'J':
        if dir == (0,1):
            mvm = [(pos[0] - 1, pos[1] - 1)]
        else:
            mvm = [(pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1), (pos[0] + 1, pos[1])]
    elif char == '-':
        if dir == (0, 1):
            mvm = [(pos[0] - 1, pos[1])]
        else:
            mvm = [(pos[0] + 1, pos[1])]
    elif char == '7':
        if dir == (-1,0):
            mvm = [(pos[0] + 1, pos[1] - 1)]
        else:
            mvm = [(pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1)]
    for m in mvm:
        if m[0] <0 or m[0] > maxX or m[1]<0 or m[1]>maxY:continue
        if m in visited: continue
        x = map[m[0]]
        y = x[:m[1]] + 'I' + x[m[1]+1:]
        map[m[0]] = y


with open('day-10/in.txt') as f:
    file = f.read().splitlines()

    maxX = len(file) - 1
    maxY = len(file[0]) - 1
    start = 0
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == 'S':
                start = (i, j) 
                break

    allPos = set()
    allPipes = []
    allPos.add(start)
    allPipes.append([start, (0,1)])
    prev, dir, cnt = start, (0,1), 0
    while True:
        newP = move(prev, dir)
        
        allPos.add(newP)
        allPipes.append([newP,dir])

        newC = file[newP[0]][newP[1]]
        if(newC == 'S'):
            break

        dir = direction(prev, newP, newC)
        prev = newP
        cnt = cnt + 1
        
    for pipe in allPipes:
        left(pipe, file, allPos)
    
    for pipe in allPipes:
        pos = pipe[0]
        x = file[pos[0]]
        y = x[:pos[1]] + 'X' + x[pos[1]+1:]
        file[pos[0]] = y

    iii = []
    for i in range(len(file)):
        for j in range(len(file[0])):
            if file[i][j] == 'I':
                iii.append((i,j))
    for i in iii:
        leak(i, file, allPos)

    cnnnt = 0
    for i in range(len(file)):
        for j in range(len(file[0])):
            if file[i][j] == 'I':
                cnnnt = cnnnt + 1
    
    print((cnt+1)/2, cnnnt)
