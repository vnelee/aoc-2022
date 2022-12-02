input = "input.txt"

# Part 1

total = 0
shape = {'X':1, 'Y':2, 'Z':3}
three_outcome = (['A','X'],['B','Y'],['C','Z'])
six_outcome = (['A','Y'],['B','Z'],['C','X'])

with open(input,'r') as file:
  for line in file:
    round = line.strip().split(' ')
    total += shape[round[1]]
    if round in three_outcome:
      total += 3
    if round in six_outcome:
      total += 6

print(total)

# Part 2

total_2 = 0
win_strat = {'A':'Y','B':'Z','C':'X'}
draw_strat = {'A':'X','B':'Y','C':'Z'}
lose_strat = {'A':'Z','B':'X','C':'Y'}

with open(input,'r') as file:
  for line in file:
    round = line.strip().split(' ')
    if round[1] == 'X':
      total_2 += shape[lose_strat[round[0]]]
    elif round[1] == 'Y':
      total_2 += shape[draw_strat[round[0]]] + 3
    else:
      total_2 += shape[win_strat[round[0]]] + 6

print(total_2)