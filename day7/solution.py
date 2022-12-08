input = "input.txt"

file_sums = {}
stack = []
ls_sum = 0
total_ans = 0

#Part 1
#brute force using stack and dict because I didn't feel like making a tree (???)
with open(input,'r') as file:
  for line in file:
    line = line.rstrip()
    if line[0] == "$" and ls_sum != 0:
      for dir in stack:
        file_sums[dir][0] += ls_sum
      file_sums[stack[-1]][1] = True
      ls_sum = 0
    if line[:4] == "$ cd":
      if line[-1] == "/":
        stack = ["/"]
        if "/" not in file_sums:
          file_sums["/"] = [0,False]
      elif line[-2:] == "..":
        stack.pop()
      else:
        dir_name = line[5:]
        if stack[-1]+dir_name not in file_sums:
          file_sums[stack[-1]+dir_name] = [0,False]
        stack.append(stack[-1]+dir_name)
    elif line[0].isdigit() and file_sums[stack[-1]][1] == False:
        ls_sum += int(line.split(" ")[0])
if ls_sum != 0:
  for dir in stack:
    file_sums[dir][0] += ls_sum

for dir in file_sums:
  if file_sums[dir][0] <= 100000:
    total_ans += file_sums[dir][0]

print(total_ans)

#Part 2
unused_space = 70000000 - file_sums["/"][0]
sums = []

for dir in file_sums:
  sums.append(file_sums[dir][0])

sums.sort()

for sum in sums:
  if unused_space + sum >= 30000000:
    print(sum)
    break