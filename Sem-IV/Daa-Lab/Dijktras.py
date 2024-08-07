n = int(input("Enter the number of vertices "))

graph = [[]*(n+1)]

e = int(input("Enter the number of edges "))

for i in range(n):
    v,wt = map(int,input().split())
    graph[]