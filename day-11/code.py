
def distance(a, b , qq,ww):
    resRows = []
    resCols = []
    lx, hx = a[0] if a[0] < b[0] else b[0], b[0] if a[0] < b[0] else a[0]
    ly, hy = a[1] if a[1] < b[1] else b[1], b[1] if a[1] < b[1] else a[1]
    for x in range(lx + 1, hx+1):
        resRows.append(x)
    for x in range(ly + 1, hy+1):
        resCols.append(x)
    x = sum([qq[a] for a in resRows])
    y = sum([ww[a] for a in resCols])
    
    return x+y

with open('day-11/in.txt') as f:
    file = f.read().splitlines()
    
    maxX, maxY = len(file), len(file[0])
    
    rows_p1 = [2 if x.count('.') == maxY else 1 for x in file ]
    rows_p2 = [1000000 if x.count('.') == maxY else 1 for x in file ]
    cols_p1, cols_p2 = [], []

    cols = []
    for i in range(maxX):
        c = ''
        for j in range(maxY):
            c = c + file[j][i]
        cols.append(c)
    cols_p1 = [2 if x.count('.') == maxY else 1 for x in cols ]
    cols_p2 = [1000000 if x.count('.') == maxY else 1 for x in cols ]

    galaxies = set()
    for i in range(maxX):
        for j in range(maxY):
            if file[i][j] == '#':
                galaxies.add((i,j))

    p1, p2 = [], []
    g_cp = galaxies.copy()
    for galaxy in galaxies:
        g_cp.remove(galaxy)
        for g in g_cp:
            if galaxy == g:
                continue
            p1_v = distance(galaxy, g, rows_p1, cols_p1)
            p2_v = distance(galaxy, g, rows_p2, cols_p2)
            p1.append(p1_v)
            p2.append(p2_v)
        
    print(sum(p1), sum(p2))

