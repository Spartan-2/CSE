def bellmanFord(graph,src,n):
    dist = [float('inf')]*(n+1)
    dist[src] = 0

    for i in range(n-1):
        for edge in graph:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
    
    for edge in graph:
        if dist[edge[1]] > dist[edge[0]] + edge[2]:
            print("Negative cycle detected ")
            return

    print("Minimum distance from the source is ")
    for i in range(n):
        print(i,"->",dist[i])
    
n = int(input("Enter the number of vertices "))
graph = []

e = int(input("Enter the number of edges "))
print("Enter the edges ")
for i in range(e):
    x = list(map(int,input().split()))
    graph.append(x)

src = int(input("Enter the source vertex "))

bellmanFord(graph,src,n)
