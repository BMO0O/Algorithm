# Python3 program to find a route by operating BFS 
# from a given matrix(map) 

import collections

# To create a queue
class Queue(object):
    def __init__(self):
        self.elements = collections.deque()

    def length(self):
        return len(self.elements)

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.popleft()

# Map for python(0 = wall or object, 1 = path)
grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,0,1,0,1,0],
        [0,0,1,0,1,0,1,1,1,0],
        [0,1,1,0,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,0]]

# Set start point and goal
start = (1,5)
goal = (8,1)

# Create a queue for BFS
queue = Queue()

# Enqueue the start node
queue.push(start)
came_from = {}

while queue.length()>0:

    # Dequeue a current vertex from queue
    current = queue.pop()

    # If find the goal, break
    if current == goal:
        break

    (x,y) = current
    # Get adjacent vertices of the dequeued vertex start.
    # If a adjacent has not been visited, then mark it came_from(=visited) 
    # and enqueue it
    candidates = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    for next in [(h,v) for h, v in candidates if grid[v][h] != 0]:
        if next not in came_from:
            queue.push(next)
            came_from[next] = current

current = goal
path = []

# Path back tracking
while current is not start:
    path.append(current)
    current = came_from[current]

# Print the path from start to goal
path.reverse()
print(path)