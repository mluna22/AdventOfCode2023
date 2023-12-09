f = open('input.txt', 'r')

sequences = f.read().strip().split('\n')
sequences = [[list(map(int, s.split(' ')))] for s in sequences]

for i in range(len(sequences)):
  while not all([sequence == 0 for sequence in sequences[i][-1]]):
    sequences[i].append([])
    for j in range(len(sequences[i][-2]) - 1):
      sequences[i][-1].append(sequences[i][-2][j+1] - sequences[i][-2][j])
  sequences[i][-1].insert(0, 0)
  for j in range(len(sequences[i]) - 2, -1, -1):
    sequences[i][j].insert(0, sequences[i][j][0] - sequences[i][j + 1][0]) 
      
sum = 0
for i in range(len(sequences)):
  sum += sequences[i][0][0]

print(sum)