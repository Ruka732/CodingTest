# insertion sort

import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

# 첫번째 원소는 이미 정렬되어 있다고 판단 - 두번째 원소부터 판별
for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    # 인덱스 i 부터 1까지 1씩 감소하며 반복, 왼쪽 원소들과 비교한다고 생각
    if arr[j] < arr[j - 1]:
      # 왼쪽 원소와 비교하여 자리 바꿈
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      
    else:
      # 더 작은 원소 만나면 break
      break

for i in arr:
  print(i)

print(arr)