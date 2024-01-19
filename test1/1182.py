import sys

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0

def subseq(idx, sub_sum):
  global cnt
  
  if idx >= n :
    return
  sub_sum += seq[idx]
  
  if sub_sum == n:
    cnt +=1 
  
  subseq(idx+1, sub_sum)
  subseq(idx+1, sub_sum-seq[idx]) # 해당 인덱스를 넘어갈 경우
  return

subseq(0, 0)
print(cnt)