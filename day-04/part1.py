input ='inputs/test.txt'
input ='inputs/input.txt'


with open(input, 'r') as f:
    file = f.read().splitlines()
    
    cardCount = [1 for e in range(len(file))]
    total = 0
    for i, line in enumerate(file):
        line = line.split(':')[1].split('|')
        win, my = line[0].split(), line[1].split() 
    
        real = [e for e in my if e in win]
        #print(win, my)
        cnt = len(real)
        if cnt > 0:
            total = total + (1 if cnt == 1 else 2**(cnt-1))
            s = i
            for x in range(i+1, i+cnt+1):
                cardCount[x] = cardCount[x] + cardCount[s] *1
        
    print(total)
    print(sum(cardCount))