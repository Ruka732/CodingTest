# 잃어버린 괄호

import sys

input = sys.stdin.readline

s = input().split('-')

num = []

for i in s:
  sum = 0
  temp = i.split('+')
  for j in temp:
    sum += int(j)
  
  num.append(sum)

n = num[0]

for i in range(1, len(num)):
  n -= num[i]

print(n)


# tokens = []
# num = ''
# for char in s:
#   if char.isdigit():
#     num += char
#   else:
#     tokens.append(num)
#     tokens.append(char)
#     num = ''
# tokens.append(num)
