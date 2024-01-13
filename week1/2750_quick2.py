import sys

sys.setrecursionlimit(10 ** 4)

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0]
  tail = arr[1:]
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x> pivot]
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

for i in quick_sort(arr):
  print(i)