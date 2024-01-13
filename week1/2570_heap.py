# heap sort

import sys

def siftdown(arr, i , size):
  l = 2*i +1 # left child
  r = 2*i +2 # right child
  largest = i
  
  if l <= size-1 and arr[l] > arr[i]:
    largest = l
  if r <= size-1 and arr[r] > arr[largest]:
    largest = r
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    siftdown

def heapify(a, size):
  # heapify 에서 노드의 절반만 확인해도 가능
  p = (size//2) - 1
  
  while p >= 0:
    siftdown(a, p, size)
    p -= 1

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

