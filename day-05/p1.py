input ='in.txt'


def getNewVal(x, map):
    for i in map:
        if i[1] <= x and i[1] + i[2] > x:
            z = x - i[1]
            return i[0] + z
    return x

with open(input, 'r') as f:
    file = f.read().splitlines()

    i = 0
    big = []
    arr = []
    while i < len(file):
        if len(file[i]) == 0:
            big.append(arr)
            arr = []
        else:
            arr.append(file[i])
        i = i + 1
    big.append(arr)

    seeds = [int(x) for x in big[0][0].split()[1:]]
    seeds = [i for i in range(79,79+13)]+[i for i in range(55,55+13)]
    print(seeds)
    soil = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[1][1:]]))
    fert = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[2][1:]]))
    wate = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[3][1:]]))
    ligh = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[4][1:]]))
    temp = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[5][1:]]))
    hum = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[6][1:]]))
    loc = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[7][1:]]))

    t1 = list(map(lambda x: getNewVal(x,soil), seeds))
    t2 = list(map(lambda x: getNewVal(x,fert), t1))
    t3 = list(map(lambda x: getNewVal(x,wate), t2))
    t4 = list(map(lambda x: getNewVal(x,ligh), t3))
    t5 = list(map(lambda x: getNewVal(x,temp), t4))
    t6 = list(map(lambda x: getNewVal(x,hum), t5))
    t7 = list(map(lambda x: getNewVal(x,loc), t6))

    print(min(t7))