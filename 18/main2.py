def translate_hex(string):
  directions = ['R','D','L','U']
  value = int(string[2:-2],16)
  dir = directions[int(string[-2])]
  return [dir, value]

def shoelace(coords):
  sum1 = 0
  sum2 = 0
  for i in range(len(coords) - 1):
    sum1 += coords[i][0] * coords[i+1][1]
    sum2 += coords[i][1] * coords[i+1][0]
  sum1 += coords[-1][0] * coords[0][1]
  sum2 += coords[0][0] * coords[-1][1]
  area = abs(sum1 - sum2) / 2
  return area

with open("input.txt", "r") as f:
  data = [translate_hex(line.split()[2]) for line in f.read().strip().split('\n')]

coords = [[0,0]]
perimeter = 0
for value in data:
  perimeter += value[1]
  if value[0] == 'R':
    coords.append([coords[-1][0], coords[-1][1] + value[1]])
  if value[0] == 'D':
    coords.append([coords[-1][0] + value[1], coords[-1][1]])
  if value[0] == 'L':
    coords.append([coords[-1][0], coords[-1][1] - value[1]])
  if value[0] == 'U':
    coords.append([coords[-1][0] - value[1], coords[-1][1]])

area = shoelace(coords) + perimeter/2 + 1
print(area)