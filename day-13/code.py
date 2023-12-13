

def compare(l, r, box, max):
    if l < 0: return True
    if r > max: return True
    res = box[l] == box[r]
    return res

def compare_p2(l, r, box, max, war):
    if l < 0: return True, war
    if r > max: return True, war
    ran, x = len(box[l]), 0
    for i in range(ran):
        x += 1 if box[l][i] == box[r][i] else 0
    res = box[l] == box[r] or x+1 == ran
    return res, war+1 if res is True and x+1 == ran else war

def get_row_col_x_y(box):
    x, y = len(box), len(box[0])
    rows, cols = box, []
    
    for ci in range(y):
        c = ''
        for r in range(x): 
            c += box[r][ci]
        cols.append(c)

    return rows, cols, len(rows), len(cols)


def box_logic(box):
    rows, cols, x, y = get_row_col_x_y(box)
    #row comp
    for i in range(1, x):
        match = True
        for j in range(x-i+1):
            match = compare(i-j-1, i+j, rows, x-1)
            if match == False:
                break
        if match == False:
            continue
        return i * 100
    
    for i in range(1, y):
        match = True
        for j in range(y-i+1):
            match = compare(i-j-1, i+j, cols, y -1)
            if match == False:
                break
        if match == False:
            continue
        return i

def box_logic_p2(box):
    rows, cols, x, y = get_row_col_x_y(box)

    #row comp
    for i in range(1, x):
        cnt, war = [], 0
        for j in range(x-i+1):
            res, war = compare_p2(i-j-1, i+j, rows, x-1, war)
            if war > 1:
                res = False
                cnt.append(res)
                break
            cnt.append(res)
        
        if all(cnt) and war == 1:
            return 100 * i

    for i in range(1, y):
        cnt, war = [], 0
        for j in range(y-i+1):
            res, war = compare_p2(i-j-1, i+j, cols, y -1, war)
            if war > 1:
                res = False
                cnt.append(res)
                break
            cnt.append(res)
            
        if all(cnt) and war == 1:
            return i


with open('day-13/in.txt') as f:
    file = f.read().split('\n\n')
    
    r1,r2 = [],[]
    for box in file:
        bos = box.splitlines()
        res1 = box_logic(bos)
        res2 = box_logic_p2(bos)
        
        r1.append(res1)
        r2.append(res2)
    print(sum(r1),sum(r2))