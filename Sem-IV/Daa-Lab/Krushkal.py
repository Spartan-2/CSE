def findParent(i):
    if parent[i] != i:
        parent[i] = findParent(parent[i])
        return parent[i]
    return parent[i]

def krushkal(g,V):
    g1 = sorted(g,key = lambda x:x[2])
    minc,i,edge = 0,0,0
    mst = []

    while edge <= V-1:
        u,v,wt = g1[i]
        i+= 1

        x,y = findParent(u),findParent(v)
        if x != y:
            mst.append([u,v,wt])
            minc += wt
            parent[x] = parent[y]
            edge += 1
        
    return mst,minc



n = int(input("Enter the number of vertices "))
parent = [i for i in range(n+1)]

e = int(input("Enter the number of edges "))
graph = []
for i in range(e):
    u,v,wt = map(int,input().split())
    graph.append([u,v,wt])

mst,cost = krushkal(graph,n)
print("The min cost tree is ",cost)
print("M S T is",mst)

