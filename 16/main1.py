DIRECTIONS = {
  'N': (-1, 0),
  'E': (0, 1),
  'S': (1, 0),
  'W': (0, -1),
}

MIRRORS = {
  '.': {
    'N': 'N',
    'S': 'S',
    'E': 'E',
    'W': 'W'
  },
  '|': {
      'N': 'N',
      'S': 'S',
      'E': 'NS',
      'W': 'NS'
    },
  '-': {
    'W': 'W',
    'E': 'E',
    'S': 'WE',
    'N': 'WE',
    },
  '/': {
    'N': 'E',
    'S': 'W',
    'E': 'N',
    'W': 'S',
    },
  '\\': {
    'N': 'W',
    'S': 'E',
    'E': 'S',
    'W': 'N',
    }
}

def throw_beam(row, column, direction, mirrors, grid):
  while row >= 0 and row < len(mirrors) and column >= 0 and column < len(mirrors[0]):
    if direction in grid[row][column]: return
    else: grid[row][column] += direction 
    mirror = mirrors[row][column]
    if len(MIRRORS[mirror][direction]) > 1:
      for dir in MIRRORS[mirror][direction]:
        throw_beam(row + DIRECTIONS[dir][0], column + DIRECTIONS[dir][1], dir, mirrors, grid)
    else:
      row += DIRECTIONS[MIRRORS[mirror][direction]][0]
      column += DIRECTIONS[MIRRORS[mirror][direction]][1]
      direction = MIRRORS[mirror][direction]

f = open('input.txt', 'r')

mirrors = [list(line) for line in f.read().strip().split('\n')]
grid = [[''] * len(mirrors[0]) for line in mirrors]

throw_beam(0, 0, 'E', mirrors, grid)

sum = 0
for line in grid:
  for dir in line:
    if dir != '': sum += 1
print(sum)

