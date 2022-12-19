import fileinput
import numpy as np
from collections import defaultdict
import heapq as heap

def BFS(adj, src, dest, v):
    queue = []
    pred = [-1] * v
    dist = [1000000] * v
  
    visited = [False for i in range(v)];
     
    visited[src] = True
    dist[src] = 0
    queue.append(src)
  
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)

        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
  
                if (adj[u][i] == dest):
                    return dist[dest]

    return -1

a = []
 
for f in fileinput.input():
    line = f[:-1]

    b = [c for c in line]
    a.append(b)

adj = []
N = len(a)
M = len(a[0])

s = 0
e = 0

for i in range(N):
    for j in range(M):
        if(a[i][j] == 'S'):
            s = i * M + j
            a[i][j] = 'a'
        if(a[i][j] == 'E'):
            e = i * M + j
            a[i][j] = 'z'

for i in range(N):
    for j in range(M):
        n = []
        c = ord(a[i][j])
        if(a[i][j] == 'S'):
            c = ord('a')

        if(a[i][j] == 'E'):
            c = ord('z')

        if(i > 0):
            if(ord(a[i-1][j]) <= c + 1):
                n.append((i - 1) * M + j)
        if(j > 0):
            if(ord(a[i][j-1]) <= c + 1):
                n.append((i) * M + (j - 1))
        if(i < N - 1):
            if(ord(a[i+1][j]) <= c + 1):
                n.append((i + 1) * M + j)
        if(j < M - 1):
            if(ord(a[i][j+1]) <= c + 1):
                n.append((i) * M + (j + 1))

        adj.append(n)

c = []

for i in range(N):
    for j in range(M):
        if(a[i][j] == 'a'):
            s = i * M + j
            v = BFS(adj, s, e, N*M)
            if v != -1:
                c.append(v)

print(min(c))