input = "input.txt"

grid = []
with open(input,'r') as file:
  for line in file:
    grid.append(line.strip())

dim = len(grid[0])

#part 1
visible = set()

def add_visible_rows(line):
  lo = 0
  lo_ptr = 1
  hi = dim-1
  hi_ptr = hi - 1

  while lo_ptr < dim-1:
    if grid[line][lo_ptr] > grid[line][lo]:
      if (line,lo_ptr) not in visible:
        visible.add((line,lo_ptr))
      lo = lo_ptr
    lo_ptr += 1
  while hi_ptr > 0:
    if grid[line][hi_ptr] > grid[line][hi]:
      if (line,hi_ptr) not in visible:
        visible.add((line,hi_ptr))
      hi = hi_ptr
    hi_ptr -= 1

def add_visible_cols(line):
  lo = 0
  lo_ptr = 1
  hi = dim-1
  hi_ptr = hi - 1

  while lo_ptr < dim-1:
    if grid[lo_ptr][line] > grid[lo][line]:
      if (lo_ptr,line) not in visible:
        visible.add((lo_ptr,line))
      lo = lo_ptr
    lo_ptr += 1
  while hi_ptr > 0:
    if grid[hi_ptr][line] > grid[hi][line]:
      if (hi_ptr,line) not in visible:
        visible.add((hi_ptr,line))
      hi = hi_ptr
    hi_ptr -= 1

for i in range(dim):
  visible.add((0,i))
  visible.add((i,0))
  visible.add((dim-1,i))
  visible.add((i,dim-1))

for i in range(1,dim-1):
  add_visible_rows(i)
  add_visible_cols(i)

print(len(visible))

#part 2
#brute force : )
best_score = 0
def score_u(i,j):
  val = grid[i][j]
  up = 0
  while i > 0:
    up += 1
    i -= 1
    if grid[i][j] >= val:
      break
  return up

def score_d(i,j):
  val = grid[i][j]
  down = 0
  while i < dim-1:
    down += 1
    i += 1
    if grid[i][j] >= val:
      break
  return down

def score_l(i,j):
  val = grid[i][j]
  l = 0
  while j > 0:
    l += 1
    j -= 1
    if grid[i][j] >= val:
      break
  return l

def score_r(i,j):
  val = grid[i][j]
  r = 0
  while j < dim-1:
    r += 1
    j += 1
    if grid[i][j] >= val:
      break
  return r

for i in range(1,dim-1):
  for j in range(1,dim-1):
    score = score_u(i,j) * score_d(i,j) * score_l(i,j) * score_r(i,j)
    best_score = max(best_score,score)

print(best_score)
    