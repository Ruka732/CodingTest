import sys

input = sys.stdin.readline

arr = []
for i in range(9):
  a = input().rstrip()
  arr.append(a)

arr.sort()
result = arr[:7]

for i in result:
  print(i)