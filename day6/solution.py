input = "input.txt"

def len_before_marker(buffer, num_chars):
  l = 0
  r = 1
  chars = set(buffer[0])
  while len(chars) < num_chars:
    if buffer[r] in chars:
      while buffer[l] != buffer[r]:
        chars.remove(buffer[l])
        l += 1
      l += 1
    else:
      chars.add(buffer[r])
    r += 1
  return r

# Part 1
with open(input,'r') as file:
  for line in file:
    print(len_before_marker(line.strip(),4))

print("---")

# Part 2
with open(input,'r') as file:
  for line in file:
    print(len_before_marker(line.strip(),14))