from functools import reduce

def count(time, distance):
    half = int(time / 2) + 1
    beat = distance
    bonus = -1 if time % 2 == 0 else 0
    for j in range(1, half):
        y = j * (time-j)
        if y > beat:
            res = (half - j) * 2 + bonus
            return res

with open('in.txt', 'r') as f:
    file = f.read().splitlines()
    
    p1t = [int(i) for i in file[0].split(':')[1].split()]
    p1d = [int(i) for i in file[1].split(':')[1].split()]

    p2t = int(''.join(str(x) for x in p1t))
    p2d = int(''.join(str(x) for x in p1d))

    counts = []
    for i,x in enumerate(p1t):
        counts.append(count(x, p1d[i]))
    
    print(reduce(lambda x, y: x*y, counts))
    print(count(p2t, p2d))