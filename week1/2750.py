# 수 정렬하기

import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

arr.sort()

for i in arr:
  print(i)