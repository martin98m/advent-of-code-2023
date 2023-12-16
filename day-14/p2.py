maxX, maxY = 0,0
def moveNorth(r, c, file):
    for i in range(r, 0, -1):
        if file[i-1][c] == '.':
            l1, l2 = file[i-1], file[i]
            file[i-1] = l1[:c] + 'O' + l1[c+1:]
            file[i] = l2[:c] + '.' + l2[c+1:]
        else:
            return file
    return file

def moveSouth(r, c, file):
    for i in range(r, maxX-1):
        if file[i+1][c] == '.':
            l1, l2 = file[i+1], file[i]
            file[i+1] = l1[:c] + 'O' + l1[c+1:]
            file[i] = l2[:c] + '.' + l2[c+1:]
        else:
            return file
    return file

def moveEast(r, c, file):
    for i in range(c, maxY-1):
        if file[r][i+1] == '.': 
            l1 = file[r]
            file[r] = l1[:i] + '.O' + l1[i+2:]
        else:
            return file
    return file

def moveWest(r, c, file):
    for i in range(c, 0, -1):
        if file[r][i-1] == '.':
            l1 = file[r]
            file[r] = l1[:i-1] + 'O.' + l1[i+1:]
        else:
            return file
    return file

with open('day-14/in.txt') as f:
    file = f.read().splitlines()
    maxX, maxY = len(file), len(file[0])

    res = file.copy()
    
    for i in range(1000000000):
        r1 = res.copy()
        for r in range(maxX):
            for c in range(maxY):
                if r1[r][c] == 'O':
                    res = moveNorth(r, c, res)

        r2 = res.copy()
        for r in range(maxX):
            for c in range(maxY):
                if r2[r][c] == 'O':
                    res = moveWest(r, c, r2)

        r3 = res.copy()
        for r in range(maxX-1,-1,-1):
            for c in range(maxY):
                if r3[r][c] == 'O':
                    res = moveSouth(r, c, r3)

        r4 = res.copy()
        for r in range(maxX):
            for c in range(maxY-1,-1,-1):
                if r4[r][c] == 'O':
                    res = moveEast(r, c, r4)
        print(i+1)
    
    
    c0 = [res[i].count('O')*(len(res)-i) for i in range(len(res))]
    print(sum(c0))