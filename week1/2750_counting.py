# counting sort

import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

count = [0] * (max(arr) + 1)

for i in range(len(arr)):
  count[arr[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i)

# 2570에선 안돌아감 : 음수가 나온다