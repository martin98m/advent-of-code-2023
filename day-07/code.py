from collections import Counter

def value(a, wild=0):
    if len(a) > 0:
        a[0] = a[0] + wild
    else:
        a.append(wild)
    if a == [5]:
        return 6
    elif a == [4,1]:
        return 5
    elif a == [3,2]:
        return 4
    elif a == [3,1,1]:
        return 3
    elif a == [2,2,1]:
        return 2
    elif a == [2,1,1,1]:
        return 1
    else:
        return 0
    
def change_sym(a, j=True):
    res = a.replace('T','B').replace('J','C' if j else '1').replace('Q','D').replace('K','E').replace('A','F')
    return res

with open('in.txt', 'r') as f:
    file = f.read().splitlines()
    
    cards, cards_p2 = [], []
    for line in file:
        keys = line.split()
        with_j = Counter(x for x in keys[0])
        res = sorted([with_j[x] for x in with_j], reverse=True)
        cards.append([change_sym(keys[0]), value(res), int(keys[1])])

        no_j = Counter(x for x in keys[0] if x != 'J')
        res = sorted([no_j[x] for x in no_j], reverse=True)
        wild = 5 - sum(res)
        cards_p2.append([change_sym(keys[0], False), value(res, wild), int(keys[1])])

    p1 = sorted(sorted(cards, key = lambda x : x[0]), key = lambda x : x[1])   
    p2 = sorted(sorted(cards_p2, key = lambda x : x[0]), key = lambda x : x[1])   
    
    p1_f, p2_f = 0, 0
    for i in range(0, len(p1)):
        p1_f = p1_f + (i+1) * p1[i][2]
        p2_f = p2_f + (i+1) * p2[i][2]
    
    print(p1_f,p2_f)