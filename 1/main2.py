f = open("input.txt", "r")
lines = f.readlines()
f.close()

numbers = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}


sum = 0
for line in range(len(lines)):
  first = ''
  last = ''
  for i in range(len(lines[line])):
    if lines[line][i].isdigit():
      first = lines[line][i]
      break
    else:
      for key in numbers:
        if lines[line][i:i+len(key)] == key:
          first = str(numbers[key])
          break
      if first != '':
        break

  for j in range(len(lines[line])-1, -1, -1):
    if lines[line][j].isdigit():
      last = lines[line][j]
      break
    else:
      for key in numbers:
        if lines[line][j-len(key)+1:j+1] == key:
          last = str(numbers[key])
          break
      if last != '': 
        break

  sum += int(first + last)
print(sum)
  