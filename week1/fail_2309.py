import sys

input = sys.stdin.readline

arr = []
for i in range(9):
  a = int(input().rstrip())
  arr.append(a)

arr.sort()

hund = sum(arr)

for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    if hund - arr[i] - arr[j] == 100:
      
      if i != j:
        arr.remove(arr[i])
        arr.remove(arr[j-1]) # arr[i]를 remove 했으므로 j-1 번째 인덱스에 원래 arr[j] 값이 들어있음
        break
    # break
# break 하고도 for 문에 진입해서 arr remove가 2번 초과

for i in arr:
  print(i)