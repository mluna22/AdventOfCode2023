f = open("input.txt", "r")

games = []

while True:
  line = f.readline()
  if not line:
      break
  line = line.strip()
  tokens = line.split(" ")
  games.append({ "game": 0, "red": 0, "green": 0, "blue": 0 })
  games[-1]["game"] = int(tokens[1][0:-1])
  for i in range(2, len(tokens), 2):
    token = tokens[i+1][0:-1] if tokens[i+1][-1] == "," or tokens[i+1][-1] == ";" else tokens[i+1] 
    games[-1][token] = max(int(tokens[i]), games[-1][token])

sumOfIds = 0
for game in games:
  if game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14:
    sumOfIds += game["game"]

print(sumOfIds)
  
