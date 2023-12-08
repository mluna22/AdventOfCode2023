f = open('input.txt', 'r')

instructions = f.readline().strip()
f.readline()

nodes = {}

while True:
  line = f.readline()
  if not line:
    break
  line = line.strip().split()
  nodes[line[0]] = (line[2][1:-1], line[3][:-1])

current_node = 'AAA'
i = 0
while current_node != 'ZZZ':
  for direction in instructions:
    i += 1
    if direction == 'L':
      current_node = nodes[current_node][0]
    if direction == 'R':
      current_node = nodes[current_node][1]
print(i)