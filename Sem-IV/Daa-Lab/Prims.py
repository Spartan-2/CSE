def Prims(graph,V,src):
    edges,cost = 0,0
    visited[src] = True
    print("The MST edges are ")
    while(edges <= V-1):
        mini,x,y = float('inf'),0,0

        for i in range(V):
            if visited[i]:
                for j in range(V):
                    if ((not visited[j]) and (graph[i][j])):
                        if graph[i][j] < mini:
                            mini = graph[i][j]
                            x,y= i,j

        cost += graph[i][j]
        print(f"{x} -> {y} {graph[x][y]}")
        edges += 1
        visited[y] = True
    print("MST cost is",cost)


n = int(input("Enter the number of vertices "))

graph = [[float('inf')]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

e = int(input("Enter the number of edges "))

for i in range(e):
    u,v,wt = map(int,input().split())
    graph[u][v] = wt
    graph[v][u] = wt
visited = [False]*(n+1)
src = int(input("Enter the source vertex"))
Prims(graph,n,src)