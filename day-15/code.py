def addLense(line, id, op, boxes):
    bx = boxes[id]
    if op == '=':
        k = line.split('=')
        for x,i in enumerate(bx):
            if i[0] == k[0]:
                bx[x] = (k[0],k[1])
                return boxes
        bx.append((k[0],k[1]))
    else:
        k = line.split('-')
        for i in bx:
            if i[0] == k[0]:
                bx.remove(i)
                break
    return boxes



with open('day-15/in.txt') as f:
    file = f.read().split(',')
    print(1,file[-1],len(file[-1]))
    total = []
    boxes = [[] for i in range(256)]
    for code in file:
        x = 0
        op = ''
        for c in code:
            op = c
            if c == '=' or c == '-':
                break
            x = x + ord(c)
            x = x * 17
            x = x % 256
        boxes = addLense(code, x, op, boxes)
        total.append(x)
    print(sum(total))
    n = 0
    for i,sh in enumerate(boxes):
        for j,b in enumerate(sh):
            print(i, j, b)
            n += (i+1) * (j+1) * int(b[1])
    print(n)

    