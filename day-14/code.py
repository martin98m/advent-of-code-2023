def moveNorth(r, c, file):
    for i in range(r, 0, -1):
        if file[i-1][c] == '.':
            l1, l2 = file[i-1], file[i]
            file[i-1] = l1[:c] + 'O' + l1[c+1:]
            file[i] = l2[:c] + '.' + l2[c+1:]
        else:
            return file
    return file

with open('day-14/in.txt') as f:
    file = f.read().splitlines()
    
    res = file.copy()
    for r in range(len(file)):
        for c in range(len(file[r])):
            a = file[r][c]
            if a == 'O':
                res = moveNorth(r, c, res)
    c0 = [res[i].count('O')*(len(res)-i) for i in range(len(res))]
    print(sum(c0))