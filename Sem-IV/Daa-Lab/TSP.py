
def TSP(graph,V,curr_pos,count,cost,path) :
    if count == V and graph[curr_pos][path[0]]:
        return cost + graph[curr_pos][path[0]],path + [path[0]]
    ans = float('inf')
    best_path = []
    for i in range(V):
        if not visited[i]:
            visited[i] = True
            new_cost,new_path = TSP(graph,V,i,count+1,cost + graph[curr_pos][i],path +[i])
            if new_cost < ans:
                ans = new_cost
                best_path = new_path
            visited[i] = False
    return ans,best_path

V = int(input("Number of vertices "))
graph = [[float('inf') for _ in range(V)] for _ in range(V)]
for i in range(V):
    graph[i][i] = 0

visited = [False]*(V+1)

src = int(input("Enter the source vertex "))
visited[src] = True

E = int(input("Enter the number of edges "))

for i in range(E):
    u,v,weight = map(int,input().split())
    graph[u][v] = weight
    graph[v][u] = weight

minCost,minPath = TSP(graph,V,src,1,0,[src])
print("Minimum cost is ",minCost)
print("Min Path Taken ","->".join(map(str,minPath)))