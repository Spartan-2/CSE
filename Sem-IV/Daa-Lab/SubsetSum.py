def subsetSum(item,W,n):
    dp = [[False]*(W+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1,n+1):
        for w in range(W+1):

            if w < item[i-1]:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w] or dp[i-1][w - item[i-1]]
    
    return dp

def findSubset(M,n,W,item):

    selected = []
    w = W

    for i in range(n,0,-1):
        if M[i][w] and not M[i-1][w]:
            selected.append(item[i-1])
            w -= item[i-1]
    return selected


n = int(input("Enter the number of weights "))
print("Enter the weights")

items = []
for i in range(n):
    items.append(int(input(f"Enter weight {i+1}")))

W = int(input("Enter the target element "))

M = subsetSum(items,W,n)

if M[n][W]:
    print("The subset exists ")
    ans = findSubset(M,n,W,items)
    print("The selected items are ",ans)
else:
    print("subset is not present")