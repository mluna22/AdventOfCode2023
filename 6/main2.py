def distance_traveled(time_pressed, race_time):
  return (race_time - time_pressed) * time_pressed

def bbsearch_left(min_time_pressed, max_time_pressed, race_time, record_distance):
  if max_time_pressed - min_time_pressed == 1:
    return min_time_pressed
  else:
    new_time_pressed = (min_time_pressed + max_time_pressed) // 2
    if distance_traveled(new_time_pressed, race_time) > record_distance:
      return bbsearch_left(min_time_pressed, new_time_pressed, race_time, record_distance)
    else:
      return bbsearch_left(new_time_pressed, max_time_pressed, race_time, record_distance)

def bbsearch_right(min_time_pressed, max_time_pressed, race_time, record_distance):
  if max_time_pressed - min_time_pressed == 1:
    return min_time_pressed
  else:
    new_time_pressed = (min_time_pressed + max_time_pressed) // 2
    if distance_traveled(new_time_pressed, race_time) > record_distance:
      return bbsearch_right(new_time_pressed, max_time_pressed, race_time, record_distance)
    else:
      return bbsearch_right(min_time_pressed, new_time_pressed, race_time, record_distance)


f = open("input.txt", "r")

time = int(f.readline()[9:].strip().replace(" ", ""))
distance = int(f.readline()[9:].strip().replace(" ", ""))

sum = bbsearch_right(0, time, time, distance) - bbsearch_left(0, time, time, distance)
print(sum)