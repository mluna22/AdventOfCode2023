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

def step(current, origin, maze):
  pipe = PIPES[maze[current[0]][current[1]]]
  direction = pipe[1 if pipe[0] == origin else 0]
  coords = DIRECTIONS[direction]
  return [current[0] + coords[0], current[1] + coords[1]], INVERSE[direction]

f = open('input.txt', 'r')

maze = []
start = [-1,-1]
for line in f:
  maze.append(list(line.strip()))
  if start[1] == -1:
    start[0] += 1
    start[1] = maze[start[0]].index('S') if 'S' in maze[start[0]] else -1

current_1 = start
current_2 = start
direction1 = ''
direction2 = ''
first = True

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

distance = 1
while current_1 != current_2:
  current_1, direction1 = step(current_1, direction1, maze)
  current_2, direction2 = step(current_2, direction2, maze)
  distance += 1

print(distance)

      

