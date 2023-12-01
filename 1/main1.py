f = open("input.txt", "r")
lines = f.readlines()
f.close()

sum = 0
for line in range(len(lines)):
  first = ''
  last = ''
  for i in range(len(lines[line])):
    if lines[line][i].isdigit():
      first = lines[line][i]
      break

  for j in range(len(lines[line])-1, -1, -1):
    if lines[line][j].isdigit():
      last = lines[line][j]
      break

  sum += int(first + last)
print(sum)
  