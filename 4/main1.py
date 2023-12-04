f = open("input.txt", "r")
lines = f.readlines()
f.close()

lines = [line.split()[2:] for line in lines]

card_size = lines[0].index('|')

points = 0
for line in lines:
  winner_count = 0
  winners = line[0:card_size]
  for card in line[card_size + 1:]:
    if card in winners:
      winner_count += 1
  points += pow(2, winner_count - 1) if winner_count > 0 else 0

print(points)