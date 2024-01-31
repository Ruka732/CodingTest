# 동전 0

import sys

input = sys.stdin.readline

n, temp = map(int, input().split())

arr = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1, -1, -1):
  if arr[i] <= temp:
    cnt += temp//arr[i]
    temp -= arr[i]*(temp // arr[i])

print(cnt)