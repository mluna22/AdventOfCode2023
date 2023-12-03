f = open("input.txt", "r")

lines = f.readlines()
for i in range(len(lines)):
  lines[i] = lines[i].replace("\n", "")

sum = 0
for line in range(len(lines)):
  char = 0
  while char < len(lines[line]):
    if lines[line][char] == '*':
      first_found = False
      space_found = False
      second_found = False
      for i in range(line - 1, line + 2):
        space_found = True
        for j in range(char - 1, char + 2):
          if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
            continue
          if lines[i][j].isdigit() and not first_found:
            space_found = False
            first_found = True
            start = j
            end = j
            while lines[i][start].isdigit():
              start -= 1
              if start < 0:
                break
            start += 1
            while lines[i][end].isdigit():
              end += 1
              if end >= len(lines[i]):
                break
            num1 = int(lines[i][start:end])
            print("num1: ", num1)
          if first_found and not lines[i][j].isdigit() and not space_found:
            space_found = True
          if first_found and space_found and lines[i][j].isdigit():
            second_found = True
            start = j
            end = j
            while lines[i][start].isdigit():
              start -= 1
              if start < 0:
                break
            start += 1
            while lines[i][end].isdigit():
              end += 1
              if end >= len(lines[i]):
                break
            num2 = int(lines[i][start:end])
            print("num2: ", num2)
            sum += num1 * num2
            print("sum: ", sum)
            break
        if second_found:
          break

    char += 1

print(sum)
        
      