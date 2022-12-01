input = "input.txt"

# Part 1
total = 0
max_cal = 0

with open(input,'r') as file:
  input_list = file.read().splitlines()

for line in input_list:
  if line == "":
    max_cal = max(max_cal, total)
    total = 0
  else:
    total += int(line)
max_cal = max(max_cal, total)

print(max_cal)

# Part 2
totals = []
total = 0
top_three = 0

for line in input_list:
  if line == "":
    totals.append(total)
    total = 0
  else:
    total += int(line)
totals.append(total)

totals.sort()

for i in range(1,4):
  top_three += totals[-i]

print(top_three)