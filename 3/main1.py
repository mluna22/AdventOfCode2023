f = open("input.txt", "r")

lines = f.readlines()
for i in range(len(lines)):
  lines[i] = lines[i].replace("\n", "")

sum = 0
for line in range(len(lines)):
  char = 0
  while char < len(lines[line]):
    if lines[line][char].isdigit():
      digit_start = char
      while lines[line][char].isdigit():  
        char += 1
        if char >= len(lines[line]):
          break
      digit_end = char
      digits = int(lines[line][digit_start:digit_end])

      for i in range(line - 1, line + 2):
        symbol_found = False
        print()
        for j in range(digit_start - 1, digit_end + 1):
          if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
            continue
          print (lines[i][j], end = "")
          if lines[i][j] != "." and not lines[i][j].isdigit():
            print("--> ", lines[i][j])
            sum += digits
            symbol_found = True
            break
        if symbol_found:
          print("digits: ", digits)
          break
      print()
    char += 1

print(sum)
        
      