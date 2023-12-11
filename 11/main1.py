def distance(a, b, doubled_rows, doubled_columns):
  distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
  start0 = min(a[0], b[0])
  end0 = max(a[0], b[0])
  start1 = min(a[1], b[1])
  end1 = max(a[1], b[1])
  for i in range(start0, end0 + 1):
    if i in doubled_rows:
      distance += 1
  for j in range(start1, end1 + 1):
    if j in doubled_columns:
      distance += 1
  return distance

f = open('input.txt', 'r')

space = []
galaxies = []
i = 0
search_start = 0
for line in f:
  space.append(list(line.strip()))
  search_start = 0
  while '#' in space[-1][search_start:]:
    search_start = space[-1].index('#', search_start)
    galaxies.append([i, search_start])
    search_start += 1
  i += 1

doubled_rows = []
doubled_columns = []
for i in range(len(space)):
  if '#' not in space[i]:
    doubled_rows.append(i)
for j in range(len(space[0])):
  if '#' not in [space[i][j] for i in range(len(space))]:
    doubled_columns.append(j)

sum = 0
for i in range(len(galaxies)):
  for j in range(i + 1, len(galaxies)):
    dist = distance(galaxies[i], galaxies[j], doubled_rows, doubled_columns)
    sum += dist
print(sum)