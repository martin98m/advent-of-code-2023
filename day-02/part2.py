
def check(arr):
    r, g, b = 0, 0, 0
    for x in range(1,len(arr),2):
        cnt, clr = int(arr[x-1]), arr[x]
        r = cnt if cnt > r and clr == 'red' else r
        g = cnt if cnt > g and clr == 'green' else g
        b = cnt if cnt > b and clr == 'blue' else b
    return [r, g, b]

def getMin(arr):
    r, g, b = 0, 0, 0
    for x in range(len(arr)):
        nr, ng, nb = arr[x][0], arr[x][1], arr[x][2]
        r = nr if nr > r else r
        g = ng if ng > g else g
        b = nb if nb > b else b
    return [r,g,b]

#input ='inputs/test.txt'
input ='inputs/input.txt'
with open(input, 'r') as f:
    file = f.read().replace(',','').splitlines()

    p1, p2 = 0, 0
    for i, line in enumerate(file):
        line = line.split(':')[1].split(';')
        x = list(map(lambda x: x.split(), line))
        y = list(map(lambda arr: check(arr), x))
        mins = getMin(y)
        p1 = p1 + (0 if mins[0]>12 or mins[1]>13 or mins[2]>14 else i + 1)
        p2 = p2 + (mins[0] * mins[1] * mins[2])
        
    print(p1)
    print(p2)
