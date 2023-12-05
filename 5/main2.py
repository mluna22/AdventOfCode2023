from numpy import sign

f = open('input.txt', 'r')
seeds_data = f.readline().split()[1:]
seeds_data = [int(seed_data) for seed_data in seeds_data]

seeds = []
for seed_start in range(0, len(seeds_data), 2):
  seeds.append([seeds_data[seed_start], seeds_data[seed_start] + seeds_data[seed_start + 1] - 1])

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
      'end': int(path_data[1]) + int(path_data[2]) - 1
    })

paths = [
  {
    'seed': 
    {
      'start': seed[0],
      'end': seed[1]
    }
  } for seed in seeds
]

for path in paths:
  for step in steps:
    [origin_step, _, destination_step] = step.split('-')
    if origin_step not in path or destination_step in path:
      continue
    path[destination_step] = {
      'start': path[origin_step]['start'],
      'end': path[origin_step]['end']
    }
    for almanac_info in almanac[step]:
      start_inside = (almanac_info['origin'] <= path[origin_step]['start'] <= (almanac_info['end']))
      end_inside = (almanac_info['origin'] <= path[origin_step]['end'] <= (almanac_info['end']))
      outside = sign(almanac_info['origin'] - path[origin_step]['start']) * sign(almanac_info['end'] - path[origin_step]['end']) == -1
      if start_inside and end_inside:
        path[destination_step]['start'] = almanac_info['destination'] + (path[origin_step]['start'] - almanac_info['origin'])
        path[destination_step]['end'] = almanac_info['destination'] + (path[origin_step]['end'] - almanac_info['origin'])
      if not start_inside and end_inside:
        paths.append(
          {
            origin_step: 
            {
              'start': path[origin_step]['start'],
              'end': almanac_info['origin'] - 1
            }
          }
        )
        path[origin_step]['start'] = almanac_info['origin']
        path[destination_step]['start'] = almanac_info['destination'] + (path[origin_step]['start'] - almanac_info['origin'])
        path[destination_step]['end'] = almanac_info['destination'] + (path[origin_step]['end'] - almanac_info['origin'])
      if start_inside and not end_inside:
        paths.append(
          {
            origin_step: 
            {
              'start': almanac_info['end'] + 1,
              'end':  path[origin_step]['end']
            }
          }
        )
        path[origin_step]['end'] = almanac_info['end']
        path[destination_step]['start'] = almanac_info['destination'] + (path[origin_step]['start'] - almanac_info['origin'])
        path[destination_step]['end'] = almanac_info['destination'] + (path[origin_step]['end'] - almanac_info['origin'])
      if not start_inside and not end_inside and outside:
        paths.append(
          {
            origin_step: 
            {
              'start': path[origin_step]['start'],
              'end': almanac_info['origin'] - 1
            }
          }
        )
        paths.append(
          {
            origin_step: 
            {
              'start': almanac_info['end'] + 1,
              'end':  path[origin_step]['end']
            }
          }
        )
        path[origin_step]['start'] = almanac_info['origin']
        path[origin_step]['end'] = almanac_info['end']
        path[destination_step]['start'] = almanac_info['destination'] + (path[origin_step]['start'] - almanac_info['origin'])
        path[destination_step]['end'] = almanac_info['destination'] + (path[origin_step]['end'] - almanac_info['origin'])

    

min_value = float('inf')
for path in paths:
  min_value = path['location']['start'] if path['location']['start'] < min_value else min_value
print(min_value)
