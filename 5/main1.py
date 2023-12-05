f = open('input.txt', 'r')
seeds = f.readline().split()[1:]

data = f.read().split('\n\n')
data = [x.strip().split('\n') for x in data]

almanac = {}
steps = []

for seed_map in data:
  map_name = seed_map[0].split()[0]
  steps.append(map_name)
  map_data = seed_map[1:]
  almanac[map_name] = []
  for path in map_data:
    path_data = path.split()
    almanac[map_name].append({
      'destination': int(path_data[0]),
      'origin': int(path_data[1]),
      'range': int(path_data[2])
    })

paths = [{'seed': int(seed)} for seed in seeds]

for step in steps:
  [origin_step, _, destination_step] = step.split('-')
  for path in paths:
    path[destination_step] = path[origin_step]
    for almanac_info in almanac[step]:
      if almanac_info["origin"] <= path[origin_step] <= (almanac_info["origin"] + almanac_info["range"] - 1):
        path[destination_step] = almanac_info["destination"] + (path[origin_step] - almanac_info["origin"])
    

min_value = float('inf')
for path in paths:
  min_value = path['location'] if path['location'] < min_value else min_value

print(min_value)