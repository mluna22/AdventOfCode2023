import numpy as np

def result(part, workflow_rules) -> str:
  for rule in workflow_rules:
    if 'variable' not in rule:
      return rule['result']
    if rule['less_than']:
      if part[rule['variable']] < rule['value']:
        return rule['result']
    else:
      if part[rule['variable']] > rule['value']:
        return rule['result']

with open("input.txt") as f:
  lines = f.read().strip().split("\n\n")
  workflows_data = lines[0].split("\n")
  parts = lines[1].split("\n")

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

parts = [{variable.split('=')[0]: int(variable.split('=')[1]) for variable in part[1:-1].split(',')} for part in parts]

sum = 0
for part in parts:
  current_workflow = workflows['in']
  while True:
    next_workflow = result(part, current_workflow)
    if next_workflow == 'A' or next_workflow == 'R':
      if next_workflow == 'A':
        sum += np.sum([part[value] for value in part])
      break
    current_workflow = workflows[next_workflow]
print(sum)