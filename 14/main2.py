from numpy import rot90
from functools import lru_cache

@lru_cache(maxsize=None)
def tilt_row(line):
  line = list(line)
  last_hash = -1
  for i in range(len(line)):
    if line[i] == '#': last_hash = i
    if line[i] == 'O':
      line[i] = '.'
      for j in range(last_hash + 1, i + 1):
        if line[j] == '.': 
          line[j] = 'O'
          break
  return line

@lru_cache(maxsize=None)
def tilt(pattern):
  pattern = [list(line) for line in pattern.split('\n')]
  pattern = rot90(pattern, 2)
  for _ in range(4):
    pattern = rot90(pattern, -1)
    for i in range(len(pattern)):
      pattern[i] = tilt_row(''.join(pattern[i]))
  pattern = rot90(pattern, 2)
  return '\n'.join([''.join(line) for line in pattern])

def load(data):
  load = 0
  data = data.split('\n')
  for i in range(len(data[0])):
    for j in range(len(data)):
      if data[j][i] == 'O': 
        load += len(data) - j
  return load

f = open('/mnt/c/Users/srmic/OneDrive/Ing Infor/4º/Advent of Code/2023/14/input.txt', 'r')

data = f.read().strip()

old_data = []
cycle_size = 0
while True:
  for tilted_done in range(len(old_data) - 1, -1, -1):
    if old_data[tilted_done] == data:
      cycle_size = len(old_data) - tilted_done
      break
  if cycle_size != 0: break
  old_data.append(data)
  data = tilt(data)

for _ in range((1000000000 - tilted_done) % cycle_size):
  data = tilt(data)

print(load(data))
