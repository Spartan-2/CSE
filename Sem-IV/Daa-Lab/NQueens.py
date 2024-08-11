def nQueens(r,n):
    if r==n:
        res.append([" ".join(row) for row in board])
        return
    for c in range(n):
        if c in col or r+c in posDiag or r-c in negDiag:
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)

        board[r][c] = 'Q'
        nQueens(r+1,n)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)

        board[r][c] = '_'
        
n = int(input("Enter the size of Chess Board "))

board = [['_']*n for _ in range(n)]

col = set()
posDiag = set()
negDiag = set()

res = []

nQueens(0,n)

print("The number of combinations ",len(res))
print("Possible positions ")
for r in res:
    print(r)