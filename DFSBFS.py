
# I havent been doing much programming(including algorithm practices due to
# personal reasons and practicing for interviews and writing personal essays...
# June 5th 2020
# Problem 1260: DFS and BFS
"""
import sys
n, m, s = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[temp[0]][temp[1]] = 1
    graph[temp[1]][temp[0]] = 1

def dfs(start, visited):
    visited += [start]
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            dfs(i, visited)
    return visited

def bfs(start):
    queue = [start]
    visited = [start]
    while queue:
        temp = queue.pop(0)
        for i in range(len(graph[temp])):
            if graph[temp][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(*dfs(s, []))
print(*bfs(s))
"""



# Problem 2606: Virus
"""
import sys

n = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = [[0]*(n+1) for i in range(n+1)]

for i in range(edge):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[temp[0]][temp[1]] = 1
    graph[temp[1]][temp[0]] = 1

def dfs(start, visited):
    visited += [start]
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            dfs(i, visited)
    return len(visited)-1

print(dfs(1, []))
"""


# Problem 2667: House number
import sys

n = int(sys.stdin.readline())
graph = []
visited = []
result = []

for i in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))

def bfs(graph, i, j, visited):

    if graph[i][j] == 0:
        visited.append([i, j])
        return [0, visited]

    block = []
    queue = [[i, j]]

    while queue:
        [i, j] = queue.pop(0)
        visited.append([i, j])
        block.append([i, j])

        if graph[i][j] == 1:
            if i < (n-1) and graph[i+1][j] == 1 and [i+1, j] not in block and [i+1, j] not in queue:
                queue.append([i+1, j])
            if j < (n-1) and graph[i][j+1] == 1 and [i, j+1] not in block and [i, j+1] not in queue:
                queue.append([i, j+1])
            if j > 0 and graph[i][j-1] ==1 and [i, j-1] not in block and [i, j-1] not in queue:
                queue.append([i, j-1])
            if i > 0 and graph[i-1][j] ==1 and [i-1, j] not in block and [i-1, j] not in queue:
                queue.append([i-1, j])

    return [len(block), visited]

for i in range(n):
    for j in range(n):
        if [i, j] not in visited:
            [total, visited] = bfs(graph, i, j, visited)
            if total != 0:
                result.append(total)


print(len(result))
final = sorted(result)
for i in range(len(result)):
    print(final[i])