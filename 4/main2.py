f = open("input.txt", "r")
lines = f.readlines()
f.close()

lines = [line.strip().split() for line in lines]

card_size = lines[0].index('|')

table = [
  {
    "winners": line[2:card_size],
    "numbers": line[card_size + 1:],
    "card_count": 1
  } for line in lines
]

card_count = 0

for game in range(len(table)):
  winner_count = 0
  for card in table[game]["numbers"]:
    if card in table[game]["winners"]:
      winner_count += 1
  for i in range(winner_count):
    if game + i + 1 >= len(table): break
    table[game + i + 1]["card_count"] += table[game]["card_count"]
  card_count += table[game]["card_count"]

print(card_count)