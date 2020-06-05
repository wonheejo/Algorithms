
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