import math

def p1_cond(p):
    return True if p == 'ZZZ' else False

with open('day-08/in.txt') as f:
    file = f.read().splitlines()

    translations = str.maketrans({'(':'', ')':'', ',':'', '=':''})
    path = list(map(lambda x: 0 if x == 'L' else 1,file[0]))
    maps = list(map(lambda x: x.translate(translations).split(), file[2:]))
    
    dict = {}
    for x in maps:
        dict[x[0]] = x[1:]

    val, cnt, l = 'AAA', 0, len(path)
    while p1_cond(val) == False:
        point = path[cnt % l]
        val = dict[val][point]
        cnt = cnt + 1

    print(cnt)
    
    starts = [a[0] for a in maps if a[0][2] == 'A']
    cnt, w, lcm_num = 1, len(starts), []
    while len(starts) > 0:
        point,rm = path[(cnt - 1) % l],[]
        for i,x in enumerate(starts):
            res=dict[x][point]
            starts[i] = res
            if res[2] == 'Z':
                lcm_num.append(cnt)
                rm.append(res)
        starts = [a for a in starts if a not in rm]
        cnt = cnt + 1

    lcm = math.lcm(*lcm_num)
    print(lcm)
    