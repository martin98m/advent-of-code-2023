maxX, maxY = 9, 9
maxX, maxY = 139, 139

def getSymbols(fileLines):
    res = []
    for i, line in enumerate(file):
        for j, c in enumerate(line):
            if c == '*':
                res.append([i, j, c])
    return res

def getSpots(x,y):
    x = x + 1 if x < 0 else x
    x = x - 1 if x > maxX else x
    y = y + 1 if y < 0 else y
    y = y - 1 if y > maxY else y

    return [x, y]

def eight(x,y):
    res = []
    for i in range(-1,2):
        for j in range(-1,2):
            res.append(getSpots(x + i, y + j))
    return res

def getNumbers(x,y, file):
    res = file[x][y]
    pos = set()
    pos.add((x,y))
    newY = y + 1
    while newY <= maxY and file[x][newY].isdigit():
        res = res + file[x][newY]
        pos.add((x,newY))
        newY = newY + 1
    newY = y - 1
    while newY >= 0 and file[x][newY].isdigit():
        res = file[x][newY] + res
        pos.add((x,newY))
        newY = newY - 1
    return (res, pos)
input ='inputs/test.txt'
input ='inputs/input.txt'

with open(input, 'r') as f:
    file = f.read().replace(',','').splitlines()
    
    symbols = getSymbols(file)
    #print(symbols)
    eights = []
    for x in symbols:
        eights.append(eight(x[0],x[1]))
    print('8:', eights)
    total = 0
    for x in eights:
        digits = list(filter(lambda x: file[x[0]][x[1]].isdigit(),x))

        nums = []
        for x in digits:
            res = getNumbers(x[0],x[1],file)
            nums.append(res)
        unique = []
        for x in nums:
            add = True
            for y in unique:
                if add is False:
                    continue
                if x[0] == y[0] and x[1] == y[1]:
                    add = False
                    continue
            if add:
                unique.append(x)
        if len(unique)  == 2:
            total = total + int(unique[0][0]) * int(unique[1][0])
    
    print(total)
    
