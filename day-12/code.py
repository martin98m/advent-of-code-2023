from itertools import product
import re

def get_var(a, b):
    var = list(product(range(a + 1), repeat=b))
    val = [x for x in var if sum(x) == a]
    return val

def dot(a):
    return f"[\\.?]{{{a}}}"

def hash(c):
    return f"[#?]{{{c}}}"

with open('day-12/in.txt') as f:
    file = f.read().splitlines()
    
    res = []
    for line in file:
        hidden, nums = line.split()[0],[int(x) for x in line.split()[1].split(',')]
        #x,y = hidden, nums
        #for i in range(4):
        #    x += '?' + hidden
        #    y = y+nums
        #hidden = x
        #nums = y

        start_v = [0]
        for i in range(len(nums)-1):
            start_v.append(1)
        start_v.append(0)

        l= len(hidden)
        s = l - sum(nums) - len(nums)+1
        var = get_var(s, len(nums) +1)
        c = 0
        for j,it in enumerate(var):
            r1 = ""
            for i,v in enumerate(nums):
                r1 = r1 + dot(it[i] + 1 if i > 0 else it[i])
                r1 = r1 + hash(v)
            r1 = r1 + dot(it[-1])

            x = re.match(r1, hidden)

            if x is None:
                continue
            c = c + 1
        #print(line, c)
        res.append(c)
    print(sum(res))

        