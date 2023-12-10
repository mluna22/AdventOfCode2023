DIRECTIONS = {
  'N': (-1, 0),
  'E': (0, 1),
  'S': (1, 0),
  'W': (0, -1),
}

INVERSE = {
  'N': 'S',
  'E': 'W',
  'S': 'N',
  'W': 'E',
}

PIPES = {
  'L': ('N', 'E'),
  '|': ('N', 'S'),
  'J': ('N', 'W'),
  '-': ('W', 'E'),
  '7': ('W', 'S'),
  'F': ('E', 'S'),
}

def opposite_end(pipe, direction):
  return PIPES[pipe][1 if PIPES[pipe][0] == direction else 0]

def step(current, origin, maze):
  coords = DIRECTIONS[opposite_end(maze[current[0]][current[1]], origin)]
  return [current[0] + coords[0], current[1] + coords[1]], INVERSE[opposite_end(maze[current[0]][current[1]], origin)]

f = open('input.txt', 'r')

maze = []
aux_maze = []
start = [-1,-1]
for line in f:
  maze.append(list(line.strip()))
  aux_maze.append([' '] * (len(line.strip())))
  if start[1] == -1: 
    start[0] += 1
    start[1] = maze[start[0]].index('S') if 'S' in maze[start[0]] else -1

current_1 = start
current_2 = start
direction1 = ''
direction2 = ''
first = True
aux_maze[start[0]][start[1]] = 'A'

# Encontrar ambas ramas
for direction in DIRECTIONS:
  pipe = maze[start[0] + DIRECTIONS[direction][0]][start[1] + DIRECTIONS[direction][1]]
  if pipe == '.': continue
  pipe_directions = PIPES[pipe]
  if INVERSE[direction] in pipe_directions:
    if first:
      current_1 = [current_1[0] + DIRECTIONS[direction][0], current_1[1] + DIRECTIONS[direction][1]]
      direction1 = INVERSE[direction]
      first = False
    else:
      current_2 = [current_2[0] + DIRECTIONS[direction][0], current_2[1] + DIRECTIONS[direction][1]]
      direction2 = INVERSE[direction]

if direction1 in ['N', 'S']:
  aux_maze[current_1[0]][current_1[1]] = direction1
else:
  aux_maze[current_1[0]][current_1[1]] = INVERSE[opposite_end(maze[current_1[0]][current_1[1]], direction1)]
if direction2 in ['N', 'S']:
  aux_maze[current_2[0]][current_2[1]] = INVERSE[direction2]
else:
  aux_maze[current_2[0]][current_2[1]] = opposite_end(maze[current_2[0]][current_2[1]], direction2)

while current_1 != current_2:
  current_1, direction1 = step(current_1, direction1, maze)
  current_2, direction2 = step(current_2, direction2, maze)
  if direction1 in ['N', 'S']:
    aux_maze[current_1[0]][current_1[1]] = direction1
  else:
    aux_maze[current_1[0]][current_1[1]] = INVERSE[opposite_end(maze[current_1[0]][current_1[1]], direction1)]
  if direction2 in ['N', 'S']:
    aux_maze[current_2[0]][current_2[1]] = INVERSE[direction2]
  else:
    aux_maze[current_2[0]][current_2[1]] = opposite_end(maze[current_2[0]][current_2[1]], direction2)

sum = 0
for i in range(len(maze)):
  inside = False
  old_aux = ' '
  for j in range(len(maze[i])):
    if aux_maze[i][j] in ['N', 'S']:
      inside = not inside if old_aux != aux_maze[i][j] else inside
      old_aux = aux_maze[i][j]
    elif aux_maze[i][j] == ' ' and inside:
      sum += 1
print(sum)

      

