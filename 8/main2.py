from functools import reduce
from math import gcd

def lcm(denominators):
  return reduce(lambda a,b: a*b // gcd(a,b), denominators)

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

current_nodes = [node for node in nodes if node[-1] == 'A']
finished_nodes = [False for node in current_nodes]
least_steps = []

i = 0
all_z = False
while not all_z:
  for direction in instructions:
    if all(finished_nodes):
      all_z = True
      break
    i += 1
    for node_pos in range(len(current_nodes)):
      if direction == 'L':
        current_nodes[node_pos] = nodes[current_nodes[node_pos]][0]
      if direction == 'R':
        current_nodes[node_pos] = nodes[current_nodes[node_pos]][1]
      if current_nodes[node_pos][-1] == 'Z':
        finished_nodes[node_pos] = True
        least_steps.append(i)

print(lcm(least_steps))