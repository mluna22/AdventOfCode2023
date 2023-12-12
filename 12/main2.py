from functools import lru_cache

@lru_cache(maxsize=None)
def recursive_check(record, groups):
  record = record.strip('.')
  if len(record) == 0: 
    if len(groups) == 0: # si no hay grupos ni caracteres
      return 1
    else:
      return 0
  elif record[0] == '?': # si hay un interrogante, probamos con un # y con un .
    return recursive_check(record.replace('?', '#', 1), groups) + recursive_check(record.replace('?', '.', 1), groups)
  elif record[0] == '#':
    if len(groups) == 0: # si no hay grupos, no puede haber #
      return 0
    elif len(record) < groups[0]: # no hay suficientes caracteres
      return 0
    elif '.' in record[:groups[0]]: # el grupo no esta completo
      return 0
    elif len(groups) > 1: # comprobamos el siguiente grupo si lo hay
      if len(record) < groups[0] + 1 or record[groups[0]] == '#': # si no hay espacio para un siguiente grupo
        return 0
      return recursive_check(record[groups[0] + 1:], groups[1:]) 
    else:
      return recursive_check(record[groups[0]:], groups[1:])
  else: return 0

f = open('input.txt', 'r')

records = []
groups = []

for line in f:
  line = line.strip().split()
  records.append('?'.join([line[0]] * 5))
  groups.append(tuple([int(n) for n in line[1].split(',')] * 5))
f.close()

sum = 0
for i in range(len(records)):
  sum += recursive_check(records[i], groups[i])

print(sum)