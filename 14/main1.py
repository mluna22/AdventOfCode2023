f = open('input.txt', 'r')

data = f.read().strip().split('\n')

load = 0
for i in range(len(data[0])):
  column_height = 0
  j = 0
  while j < len(data):
    if data[j][i] == 'O': 
      load += len(data) - column_height
      column_height += 1
    if data[j][i] == '#':
      column_height = j + 1
    j += 1

print(load)