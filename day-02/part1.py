r, g, b = 12, 13, 14

def check(arr):
    for x in range(1,len(arr),2):
        cnt, clr = int(arr[x-1]), arr[x]
        if  clr == 'red' and cnt > r:
            return False
        if clr == 'green' and cnt > g:
            return False
        if clr == 'blue' and cnt > b:
            return False
    return True

#input ='inputs/test.txt'
input ='inputs/input.txt'

with open(input, 'r') as f:
    file = f.read().replace(',','').splitlines()

    total = 0
    for x, line in enumerate(file):
        line = line.split(':')[1].split(';')
        inp = list(map(lambda x: x.split(),line))
        res = list(map(lambda arr: check(arr), inp))
        if all(res):
            total = total + x + 1 
    
    print(total)
