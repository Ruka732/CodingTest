# ATM
import sys

input = sys.stdin.readline

n = int(input())

procedure = list(map(int, input().split()))
modified = []
for idx, time in enumerate(procedure):
  modified.append([time, idx+1])

modified.sort()
# print(modified)

result = 0
arr = []
for i in range(len(modified)):
  result = result + modified[i][0]
  arr.append(result)

print(sum(arr))