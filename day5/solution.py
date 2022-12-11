import re, copy

input = "input.txt"

with open(input,'r') as file:
  input_string = file.read()

stacks_input = input_string.split("\n\n")[0].split("\n")

num_stacks = int(stacks_input[-1][-2])

stacks = [[]] * num_stacks

# Index 0 will be top of stack
for i in range(len(stacks_input)-1):
  idx = 1
  s = 1
  while idx < len(stacks_input[i]):
    if stacks_input[i][idx] != " ":
      stacks[s-1] = stacks[s-1] + [stacks_input[i][idx]]
    idx += 4
    s += 1

instructions = []
for i in input_string.split("\n\n")[1].split("\n"):
  instructions.append(re.findall("[0-9]+", i))

# Part 1
def move_pt1():
  stacks_pt1 = copy.deepcopy(stacks)
  for i in instructions:
    for mv in range(int(i[0])):
      stacks_pt1[int(i[2])-1].insert(0,stacks_pt1[int(i[1])-1].pop(0))
  ans = ""
  for s in stacks_pt1:
    ans += s[0]
  return(ans)

print(move_pt1())

# Part 2
def move_pt2():
  stacks_pt2 = copy.deepcopy(stacks)
  for i in instructions:
    tmp = stacks_pt2[int(i[1])-1][:int(i[0])][::-1]
    for t in tmp:
      stacks_pt2[int(i[1])-1].pop(0)
      stacks_pt2[int(i[2])-1].insert(0,t)
  ans = ""
  for s in stacks_pt2:
    ans += s[0]
  return(ans)

print(move_pt2())