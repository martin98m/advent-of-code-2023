
#file = open('inputs/test2.txt', 'r', encoding='utf-8').read().splitlines()
file = open('inputs/input.txt', 'r', encoding='utf-8').read().splitlines()
nums = []
for line in file:
    left = ''
    for c in line:
        left = left + c
        for word,num in {'one':'1','two':'2','three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}.items() :
            left = left.replace(word,num)
    x = [s for s in list(left) if s.isdigit()]
    right = ''
    for c in line[::-1]:
        right = c + right
        for word,num in {'one':'1','two':'2','three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}.items() :
            right = right.replace(word,num)
    
    y = [s for s in list(right) if s.isdigit()]
    
    nums.append(int(x[0]+y[-1]))

print(sum(nums))