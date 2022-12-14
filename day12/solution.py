input = 'input.txt'

grid = []

with open(input,'r') as file:
  for i,line in enumerate(file):
    if "S" in line:
      start = [i,line.index("S")]
    if "E" in line:
      end = [i,line.index("E")]
    grid.append(line.strip())

row = len(grid)
col = len(grid[0])

grid[start[0]] = grid[start[0]][:start[1]] + 'a' + grid[start[0]][start[1]+1:]
grid[end[0]] = grid[end[0]][:end[1]] + 'z' + grid[end[0]][end[1]+1:]

# Part 1
def bfs():
  visited = set()
  q = []
  q.append((start[0],start[1],0))
  while q:
    pop = q.pop(0)
    i,j,length = pop[0], pop[1], pop[2]
    if [i,j] == end:
      return length
    for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
      if (x,y) not in visited and 0<=x<row and 0 <=y<col and (ord(grid[x][y]) <= ord(grid[i][j]) + 1):
        q.append((x,y,length+1))
        visited.add((x,y))

print(bfs())

# Part 2
def bfs_2():
  visited = set()
  min_length = row*col
  q = []
  q.append((end[0],end[1],0))
  while q:
    pop = q.pop(0)
    i,j,length = pop[0], pop[1], pop[2]
    if grid[i][j] == 'a':
      min_length = min(length, min_length)
    for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
      if (x,y) not in visited and 0<=x<row and 0 <=y<col and (ord(grid[x][y]) >= ord(grid[i][j]) - 1):
        q.append((x,y,length+1))
        visited.add((x,y))
  return min_length

print(bfs_2())