def Hash(string):
  current_value = 0
  for c in string:
    current_value += ord(c)
    current_value *= 17
    current_value = current_value % 256
  return current_value

f = open('input.txt', 'r')

steps = f.read().strip().split(',')

boxes = {}

for step in steps:
  value = ('',0)
  value = (step[:-1],0) if step[-1] == '-' else (step[:step.find('=')], int(step[step.find('=') + 1]))
  hash_key = Hash(value[0])
  value_found = False
  for lens in range(len(boxes[hash_key] if hash_key in boxes else [])):
    if boxes[hash_key][lens][0] == value[0]:
      value_found = True
      if step[-1] == '-':
        boxes[hash_key].remove(boxes[hash_key][lens])
      else:
        boxes[hash_key][lens] = value
      break
  if not value_found and step[-1] != '-': 
    if hash_key in boxes: boxes[hash_key].append(value)
    else: boxes[hash_key] = [value]

sum = 0
for box in boxes:
  if len(boxes[box]) > 0:
    for i in range(len(boxes[box])):
      sum += (box + 1) * (i + 1) * (boxes[box][i][1])
print(sum)