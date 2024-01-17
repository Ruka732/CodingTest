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
        # break
        for x in arr:
          print(x)
        exit()
    # break
# break 하고도 for 문에 진입해서 arr remove가 2번 초과
# for i in arr:
#   print(i)

# 만족하는 i, j를 찾은 이후 if문만 break 하고 다시 for 문으로 돌아가서 이 후 만족하는
# i, j를 찾아서 remove 한듯.
# 그래서 찾자마자 출력하고 프로그램 종료시킴