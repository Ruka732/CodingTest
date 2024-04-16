# 단어 수학
import sys

input = sys.stdin.readline

n = int(input())

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

words = []
for _ in range(n):
  words.append(list(map(str, input().strip())))

words_count = dict()

for word in words:
  l = len(word) - 1
  
  for alpha in word:
    if alpha in words_count:
      words_count[alpha] += 10 ** l
    else:
      words_count[alpha] = 10 ** l
    
    l -= 1

words_count = sorted(words_count.values(), reverse=True)
result = 0
curr_num = 9

for i in words_count:
  result += i * curr_num
  curr_num -= 1

print(result)