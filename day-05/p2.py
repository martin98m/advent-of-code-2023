
def create_intervals(x):
    return [x[1], x[1] + x[2] - 1, x[0], x[0] + x[2] - 1]

def get_overlap(a, b):
    if a[0] > b[1] or a[1] < b[0]:
        return
    x = sorted([a[0], a[1], b[0], b[1]])
    return [x[1], x[2]]

def change_val(inetrval, sito):
    size = inetrval[1] - inetrval[0]
    sito_diff = abs(sito[0] - inetrval[0])
    new_int = [sito[2] + sito_diff, sito[2] + sito_diff + size]
    return new_int

def traverse_sitos(interval, sitos):
    res = interval
    for s in sitos:
        if interval[0] >= s[0] and interval[1] <= s[1]:
            return change_val(interval, s)
    return res

def fill_void(a,b):
    sito = sorted(b,key=lambda x: x[0])
    filled = []
    min = a[0]
    for s in sito:
        if s[0] > min:
            max = s[0]
            filled.append([min,max-1])
            filled.append([s[0],s[1]])
            min = s[1] + 1
        else:
            filled.append([s[0],s[1]])
            min = s[1] + 1
    if min < a[1]:
        filled.append([min,a[1]])
    
    return filled

def find_path(interval, sito):
    intervals = []
    for s in sito:
        new_int = get_overlap(interval, s[:2])
        if new_int is not None:
            intervals.append(new_int)
    return fill_void(interval, intervals)

with open('in.txt', 'r') as f:
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

    seed_intervals = [[seeds[x], seeds[x]+ seeds[x+1] - 1] for x in range(0, len(seeds), 2)] 
    seed_intervals_p1 = [[seeds[x], seeds[x]] for x in range(0, len(seeds))] 

    soil = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[1][1:]]))
    soil_intervals = [create_intervals(x) for x in soil]
    fert = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[2][1:]]))
    fert_intervals = [create_intervals(x) for x in fert]
    wate = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[3][1:]]))
    wate_intervals = [create_intervals(x) for x in wate]
    ligh = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[4][1:]]))
    ligh_intervals = [create_intervals(x) for x in ligh]
    temp = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[5][1:]]))
    temp_intervals = [create_intervals(x) for x in temp]
    hum = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[6][1:]]))
    hum_intervals = [create_intervals(x) for x in hum]
    loc = list(map(lambda x: [int(a) for a in x], [x.split() for x in big[7][1:]]))
    loc_intervals = [create_intervals(x) for x in loc]
    
    sita = [soil_intervals, fert_intervals, wate_intervals, ligh_intervals, temp_intervals, hum_intervals, loc_intervals]
    res, remap = 0, seed_intervals#_p1
    for sito in sita:
        res = list(map(lambda x: find_path(x, sito), remap))
        res = [b for b in res for b in b]
        remap = list(map(lambda x: traverse_sitos(x, sito),res))
    res = [b for b in remap for b in b]
    print(min(res))
    