input ='inputs/test.txt'
input ='inputs/input.txt'

with open(input, 'r') as f:
    file = f.read().splitlines()

    cardCount = [1] * len(file)
    total = 0
    for i, line in enumerate(file):
        line = line.split(':')[1].split('|')
        win, my = line[0].split(), line[1].split()

        count = len([e for e in my if e in win])
        if count > 0:
            total = total + 2**(count-1)
            for x in range(i + 1, i + count + 1):
                cardCount[x] = cardCount[x] + cardCount[i]
    
    print(total)
    print(sum(cardCount))