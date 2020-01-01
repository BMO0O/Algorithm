# Python3 program for A* source shortest path algoritm.
# The program is for adjacency matrix representation of the graph 
import heapq

# Class to make queue
class Queue(object):
    def __init__(self):
        self.elements = []

    def length(self):
        return len(self.elements)

    def push(self, x, priority):
        heapq.heappush(self.elements, (priority, x))

    def pop(self):
        return heapq.heappop(self.elements)[1]

# sample map to test A* algorithm

#grid = [[0,0,0,0,0,0,0,0,0,0],
#        [0,1,1,1,1,1,1,1,1,0],
#        [0,3,0,0,0,0,2,0,1,0],
#        [0,3,1,1,1,0,1,0,1,0],
#        [0,0,1,0,1,0,1,1,1,0],
#        [0,1,1,0,1,1,1,0,1,0],
#        [0,0,0,0,0,0,0,0,0,0]]

grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]


# set the starting point and goal
start = (1, 5)
goal = (8,1)

queue = Queue()
queue.push(start, 0)
came_from = {}
cost_so_far = {}
cost_so_far[start] = 0

# A utility function to calculate a cost of the routh from the set of vertices to adjacent vertex
def calc_cost(current, next):
    (x,y) = next
    return cost_so_far[current] + grid[y][x]

# A utility function to calculate Heuristic distance 
def heuristic(goal, next):
    (x1, y1) = goal
    (x2, y2) = next
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy

# Until the current point reaches to the goal point, update the minimum distance route   
while queue.length() > 0:
    current = queue.pop()

    if current == goal:
        break

    (x, y) = current
    candidates = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    for next in [(h,v) for h, v in candidates if grid[v][h] != 0]:
        new_cost = calc_cost(current, next)
        if next not in came_from or new_cost < cost_so_far[next]:

            # a precedence value is a sum of cumulative cost and heuristic 
            queue.push(next, new_cost + heuristic(goal, next))

            # Pick the minimum distance from the set of vertices not yet processed
            cost_so_far[next] = new_cost
            came_from[next] = current

current = goal
path = []

# Put the minimum distance route in the shortest path queue. 
while current is not start:
    path.append(current)
    current = came_from[current]

path.reverse()
print(path)