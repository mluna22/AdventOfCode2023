from functools import reduce
from copy import deepcopy

def dfs(workflows, current_part, current_workflow):
  sum = 0
  if current_workflow == 'A':
    return reduce(lambda a, b: a * b ,[current_part[value][1] - current_part[value][0] + 1 for value in current_part])
  if current_workflow == 'R':
    return 0
  for rule in workflows[current_workflow]:
    if 'variable' not in rule:
      return sum + dfs(workflows, current_part, rule['result'])
    new_part = deepcopy(current_part)
    if rule['less_than']:
      if rule['value'] < new_part[rule['variable']][1]:
        new_part[rule['variable']][1] = rule['value'] - 1
        current_part[rule['variable']][0] = rule['value']
      if rule['value'] <= new_part[rule['variable']][0]:
        return 0
    else:
      if rule['value'] > new_part[rule['variable']][0]:
        new_part[rule['variable']][0] = rule['value'] + 1
        current_part[rule['variable']][1] = rule['value']
      if rule['value'] >= new_part[rule['variable']][1]:
        return 0
    sum += dfs(workflows, new_part, rule['result'])
  return sum

with open("input.txt") as f:
  lines = f.read().strip().split("\n\n")
  workflows_data = lines[0].split("\n")

workflows = {}
for i in range(len(workflows_data)):
  workflow_name = workflows_data[i].split('{')[0]
  workflow_rules = workflows_data[i].split('{')[1].split('}')[0].split(',')
  for j in range(len(workflow_rules)):
    if ':' not in workflow_rules[j]:
      workflow_rules[j] = { 'result': workflow_rules[j] }
      continue
    less_than = '<' in workflow_rules[j]
    sign_pos =  workflow_rules[j].index('<') if less_than else workflow_rules[j].index('>')
    sep_pos = workflow_rules[j].index(':')
    workflow_rules[j] = {
      'variable': workflow_rules[j][:sign_pos],
      'value': int(workflow_rules[j][sign_pos+1:sep_pos]),
      'less_than': less_than,
      'result': workflow_rules[j][sep_pos+1:]
    }
  workflows[workflow_name] = workflow_rules

sum = 0
current_workflow = 'in'
initial_part = { 
  'x': [1,4000], 
  'm': [1,4000], 
  'a': [1,4000],
  's': [1,4000]
}

sum = dfs(workflows, initial_part, current_workflow)

print(sum)