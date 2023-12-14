from numpy import transpose

def difference(m, n):
  diff = 0
  for i in range(min(len(m),len(n))):
    if m[i] != n[i]: diff += 1
  return diff + abs(len(m) - len(n))

def transpose_strings(strings):
  return [''.join(arr) for arr in transpose([list(line) for line in strings])]

f = open('input.txt', 'r')

patterns = [[''.join(['1' if c == '#' else '0' for c in line]) for line in pattern.split('\n')] for pattern in f.read().strip().split('\n\n')]

num_horiz = 0
num_vert = 0
reflexion_found = False
for pattern in patterns:
  reflexion_found = False
  for i in range(len(pattern) - 1):
    if pattern[i] == pattern[i + 1] or difference(pattern[i], pattern[i + 1]) == 1:
      j = 0
      reflexion_found = True
      smudge_counter = 0
      while i + j + 1 < len(pattern) and i - j >= 0:
        if difference(pattern[i + j + 1], pattern[i - j]) == 1:
          smudge_counter += 1
        elif pattern[i + j + 1] != pattern[i - j]: 
          reflexion_found = False
          break
        j += 1
      if reflexion_found and smudge_counter == 1: 
        num_horiz += i + 1
        break
  
  if reflexion_found and smudge_counter == 1: continue
  pattern = transpose_strings(pattern)
  for i in range(len(pattern) - 1):
    if pattern[i] == pattern[i + 1] or difference(pattern[i], pattern[i + 1]) == 1:
      j = 0
      reflexion_found = True
      smudge_counter = 0
      while i + j + 1 < len(pattern) and i - j >= 0:
        if difference(pattern[i + j + 1], pattern[i - j]) == 1:
          smudge_counter += 1
        elif pattern[i + j + 1] != pattern[i - j]: 
          reflexion_found = False
          break
        j += 1
      if reflexion_found and smudge_counter == 1:
        num_vert += i + 1
        break

print('resultado: ', num_horiz * 100 + num_vert)