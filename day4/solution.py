import re

input = "input.txt"

# Part 1
num_pairs = 0
with open(input,'r') as file:
  for line in file:
    line = re.split(',|-',line)
    rng_1 = range(int(line[0]),int(line[1])+1)
    rng_2 = range(int(line[2]),int(line[3])+1)
    if all(i in rng_1 for i in rng_2) or all(i in rng_2 for i in rng_1):
      num_pairs += 1

print(num_pairs)

# Part 2
num_overlap_pairs = 0
with open(input,'r') as file:
  for line in file:
    line = re.split(',|-',line)
    rng_1 = range(int(line[0]),int(line[1])+1)
    rng_2 = range(int(line[2]),int(line[3])+1)
    if not set(rng_1).isdisjoint(rng_2):
      num_overlap_pairs += 1

print(num_overlap_pairs)