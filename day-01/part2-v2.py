
dict = {'one':'1','two':'2','three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}.items()

def getNumber(line, left):
    x = ''
    for c in line:
        if c.isdigit():
            return c
        x = x + c if left else c + x
        for word,num in dict:
            res = x.find(word)
            if res != -1:
                return num

#input = 'inputs/test2.txt'
input = 'inputs/input.txt'

with open(input, 'r') as f:
    file = f.read().splitlines()

    nums = []
    for line in file:
        resL = getNumber(line, True)
        resR = getNumber(line[::-1], False)
        nums.append(int(resL+resR))

    print(sum(nums))
