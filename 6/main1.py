def distance_traveled(time_pressed, race_time):
  return (race_time - time_pressed) * time_pressed


f = open("input.txt", "r")

time = list(map(lambda x: int(x), f.readline().split()[1:]))
distance = list(map(lambda x: int(x), f.readline().split()[1:]))

result = 1
for i in range(len(time)):
  sum = 0
  for j in range(time[i]):
    if distance_traveled(j, time[i]) > distance[i]:
      sum += 1
  result *= sum
print(result)