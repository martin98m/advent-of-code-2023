def p1_cond(arr):
    return len(arr) == len([a for a in arr if a == 0])

with open('in.txt') as f:
    file = f.read().splitlines()

    fin1, fin2 = [], []
    for line in file:
        line, last, first = [int(a) for a in line.split()], [], []
        while True:
            ln = len(line) - 1
            a = [0] * ln
            for i in range(0, ln):
                a[i] = line[i+1] - line[i]
            first.append(line[0])
            last.append(line[-1])
            line = a
            if p1_cond(a):
                break
        
        fin1.append(sum(last))
        res = list(map(lambda x: first[x] if ((x % 2) == 0) else -first[x], range(len(first))))
        fin2.append(first[0] + sum(res[1:]))

    print(sum(fin1),sum(fin2))