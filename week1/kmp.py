# kmp

def kmp(txt, pat):
  # kmp_table
  table = [0 for _ in range(len(pat))]
  i = 0
  
  for j in range(1, len(pat)):
    while i > 0 and pat[i] != pat[j]:
      i = table[i-1]
    
    if pat[i] == pat[j]:
      i += 1
      table[j] = i
      # [0, 0, 0, 1, 0]
  
  # kmp
  result = []
  i = 0
  for j in range(len(txt)):
    while i > 0 and pat[i] != txt[j]:
      i = table[i - 1]
      
    if pat[i] == txt[j]:
      i += 1
      if i == len(pat):
        result.append(j - i + 1)
        i = table[i - 1]
    
  return result

print(kmp('abbaacabbacaab', 'abbac'))
