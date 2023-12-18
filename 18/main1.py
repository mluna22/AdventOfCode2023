with open("test.txt", "r") as f:
  data = [[line.split()[0], int(line.split()[1])] for line in f.read().strip().split('\n')]

def expand(matrix, rows, cols):
  if rows < 0:
    matrix = [[' '] * len(matrix[0]) for i in range(abs(rows))] + matrix
  elif rows > 0:
    matrix = matrix + [[' '] * len(matrix[0]) for i in range(rows)]
  if cols < 0:
    for i in range(len(matrix)):
      matrix[i] = [' '] * abs(cols) + matrix[i]
  elif cols > 0:
    for i in range(len(matrix)):
      matrix[i] = matrix[i] + [' '] * cols
  return matrix

def get_area(matrix):
  area = 0
  for i in range(len(matrix)):
    j = 0
    while j < len(matrix[i]):
      if matrix[i][j] in 'UD' and matrix[i][j] == 'U':
        area += 1
        j += 1
        while matrix[i][j] != 'D':
          matrix[i][j] = '#'
          area += 1
          j += 1
        while j < len(matrix[i]) and matrix[i][j] != ' ':
          if matrix[i][j] == 'U': 
            j -= 1
            break
          matrix[i][j] = '#'
          area += 1
          j += 1
      j += 1
  return matrix, area

aux = [[' ']]
row = 0
col = 0
for line in data:
  if line[0] == 'R':
    if row == 150:
      print(col, line[1])
    if len(aux[row]) < col + line[1] + 1:
      aux = expand(aux, 0, col + line[1] + 1 - len(aux[row]))
    for col in range(col + 1, col + line[1] + 1):
      aux[row][col] = 'R'
  if line[0] == 'L':
    if col - line[1] < 0:
      aux = expand(aux, 0, col - line[1])
      col = line[1]
    for col in range(col - 1, col - line[1] - 1, -1):
      aux[row][col] = 'L'
  if line[0] == 'U':
    if row - line[1] < 0:
      aux = expand(aux, row - line[1], 0)
      row = line[1]
    for row in range(row, row - line[1] - 1, -1):
      aux[row][col] = 'U'
  if line[0] == 'D':
    if len(aux) < row + line[1] + 1:
      aux = expand(aux, row + line[1] + 1 - len(aux), 0)
    for row in range(row, row + line[1] + 1):
      aux[row][col] = 'D'
    
o = open('output.txt', 'w')
aux, area = get_area(aux)
print(area)
print('\n'.join([''.join(row) for row in aux]), file=o)