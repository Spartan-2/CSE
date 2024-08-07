def knapsack(item,n,W):

    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(1,n+1):
        for w in range(W+1):

            if item[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - item[i-1][1]] + item[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    
    w = W
    selected = []
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(item[i-1])
            w -= item[i-1][1]
    
    selected.reverse()

    print("The max value obtained is ",dp[n][W])
    print("The items selected are ",selected)




n = int(input("Enter the number of items "))

items = []

print("Enter the items (weight,value)")
for i in range(n):
    w,v = map(int,input(f"Item {i+1}").split())
    items.append([i+1,w,v])

W = int(input("Enter the knapsack size "))

knapsack(items,n,W)