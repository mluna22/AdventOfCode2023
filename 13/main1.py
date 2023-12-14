from numpy import transpose

def transpose_strings(strings):
  return [''.join(arr) for arr in transpose([list(line) for line in strings])]

f = open('/mnt/c/Users/srmic/OneDrive/Ing Infor/4º/Advent of Code/2023/13/input.txt', 'r')

patterns = [[''.join(['1' if c == '#' else '0' for c in line]) for line in pattern.split('\n')] for pattern in f.read().strip().split('\n\n')]

num_horiz = 0
num_vert = 0
reflexion_found = False
for pattern in patterns:
  reflexion_found = False
  for i in range(len(pattern) - 1):
    if pattern[i] == pattern[i + 1]:
      j = 0
      reflexion_found = True
      while i + j + 1 < len(pattern) and i - j >= 0:
        if pattern[i + j + 1] != pattern[i - j]: 
          reflexion_found = False
          break
        j += 1
      if reflexion_found: 
        num_horiz += i + 1
        break
  
  if reflexion_found: continue
  pattern = transpose_strings(pattern)
  for i in range(len(pattern) - 1):
    if pattern[i] == pattern[i + 1]:
      j = 0
      reflexion_found = True
      while i + j + 1 < len(pattern) and i - j >= 0:
        if pattern[i + j + 1] != pattern[i - j]: 
          reflexion_found = False
          break
        j += 1
      if reflexion_found:
        num_vert += i + 1
        break

print(num_horiz * 100 + num_vert)