input = "input.txt"

#part 1
total = 0
cycle = 0
tgt_cycle = 20
x = 1

with open(input,'r') as file:
  for line in file:
    line = line.strip().split(' ')
    if len(line) == 1:
      cycle += 1
    else:
      if cycle + 2 >= tgt_cycle:
        total  += x * tgt_cycle
        tgt_cycle += 40
      x += int(line[1])
      cycle += 2

print(total)

#part 2
img = ""
cycle = 1
x = 1

def write():
  tmp = ""
  if cycle != 1 and (cycle - 1)%40 == 0:
    tmp += "\n"
  if (cycle-1)%40 in range(x-1,x+2):
    tmp += "#"
  else:
    tmp += "."
  return tmp

with open(input,'r') as file:
  for line in file:
    line = line.strip().split(' ')
    img += write()
    if len(line) == 1:
      cycle += 1
    else:
      cycle += 1
      img += write()
      x += int(line[1])
      cycle += 1
print(img)