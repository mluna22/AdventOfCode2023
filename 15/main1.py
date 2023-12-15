def Hash(string):
  current_value = 0
  for c in string:
    current_value += ord(c)
    current_value *= 17
    current_value = current_value % 256
  return current_value

f = open('input.txt', 'r')

steps = f.read().strip().split(',')

sum = 0
for step in steps:
  sum += Hash(step)

print(sum)