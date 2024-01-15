# 단어 정렬

import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
  word = str(input().rstrip())
  arr.append(word)

# 중복 단어 제거
arr = list(set(arr))
# sort : 문자열 오름차순
arr.sort()
# key 조건에 따라 sort
arr.sort(key=len)

for i in arr:
  print(i)