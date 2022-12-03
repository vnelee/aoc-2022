input = "input.txt"

# Part 1
total = 0

with open(input,'r') as file:
  for line in file:
    sack = line.strip()
    cmpt_one = set()
    for i in range((len(sack)//2)):
      cmpt_one.add(sack[i])
    for i in range(len(sack)//2,len(sack)):
      if sack[i] in cmpt_one:
        if sack[i].isupper():
          total += ord(sack[i]) - 38
        else:
          total += ord(sack[i]) - 96
        break

print(total)

# Part 2
total_two = 0
elf_one = set()
elf_two = set()
counter = 1

with open(input,'r') as file:
  for line in file:
    sack = line.strip()
    if counter == 1:
      for type in sack:
        elf_one.add(type)
      counter += 1
    elif counter == 2:
      for type in sack:
        if type in elf_one:
          elf_two.add(type)
      counter += 1
    else:
      for type in sack:
        if type in elf_two:
          if type.isupper():
            total_two += ord(type) - 38
          else:
            total_two += ord(type) - 96
          break
      counter = 1
      elf_one.clear()
      elf_two.clear()

print(total_two)