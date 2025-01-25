from collections import deque

maze = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
]
start = (0, 0)
end = (3, 0)
"""
maze = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
start = (0, 0)
end = (2, 2)

maze = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
    ]
start = (0, 0)
end = (2, 2)

maze = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1]
    ]
start = (0, 0)
end = (4, 4)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1]
    ]
start = (0, 0)
end = (7, 7)

maze = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
]
start = (0, 0)
end = (3, 0)
"""
for row in maze:
    print(row)

rows, cols = len(maze), len(maze[0])
start_x, start_y = start
end_x, end_y = end

if start == end:
    print("Shortest distance:", 0)
    print("Path taken:", [start])
    exit()

if maze[start_x][start_y] == 0 or maze[end_x][end_y] == 0:
    print("Shortest distance:", -1)
    print("No path found.")
    exit()

visited = [[False for _ in range(cols)] for _ in range(rows)]
visited[start_x][start_y] = True
parent = {}  

queue = deque()
queue.append((start_x, start_y, 0))
path_found = False
final_dist = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue and not path_found:
    x, y, dist = queue.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if not visited[nx][ny] and maze[nx][ny] == 1:
                parent[(nx, ny)] = (x, y)
                if (nx, ny) == (end_x, end_y):
                    path_found = True
                    final_dist = dist + 2
                    break
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

if path_found:
    path = []
    curr = (end_x, end_y)
    while curr in parent:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    print("Shortest distance:", final_dist)
    print("Path taken:", path[::-1])
else:
    print("Shortest distance:", -1)
    print("No path found.")




