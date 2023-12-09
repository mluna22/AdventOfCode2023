f = open('input.txt', 'r')

sequences = f.read().strip().split('\n')
sequences = [[list(map(int, s.split(' ')))] for s in sequences]

for i in range(len(sequences)):
  while not all([sequence == 0 for sequence in sequences[i][-1]]):
    sequences[i].append([])
    for j in range(len(sequences[i][-2]) - 1):
      sequences[i][-1].append(sequences[i][-2][j+1] - sequences[i][-2][j])
      
sum = 0
for i in range(len(sequences)):
  for j in range(len(sequences[i])):
    sum += sequences[i][j][-1]

print(sum)