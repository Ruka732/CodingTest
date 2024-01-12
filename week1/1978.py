# 소수 찾기

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
result = 0

for i in arr:
    for j in range(2, i+1):
      if i % j == 0:
        if i == j:
          result += 1
        break

print(result)