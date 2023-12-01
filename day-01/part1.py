
#file = open('inputs/test1.txt', 'r', encoding='utf-8').read().splitlines()
file = open('inputs/input.txt', 'r', encoding='utf-8').read().splitlines()
nums = []
for line in file:
    x = [s for s in list(line) if s.isdigit()]
    nums.append(int(x[0]+x[-1]))

print(sum(nums))