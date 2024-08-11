def OPT(n):
    if n == 0:
        return 0
    if M[n] >= 1:
        return M[n]
    else:
        M[n] = max(OPT(n-1),jobs[n-1][2] + OPT(p(n)))
        return M[n]

def weightSche(job):
    
    sorted(job,key = lambda x:x[1])
    profit = OPT(len(job))
    return profit

def selection(k):
    if k <1:
        return 
    if jobs[k-1][2] + M[p(k)] >= M[k-1]:
        selected.append(jobs[k-1])
        selection(p(k))
    else:
        selection(k-1)
        
def p(k):

    for i in range(k-1,-1,-1):
        if jobs[k-1][0] >= jobs[i-1][1]:
            return i
    return 0

n = int(input("Enter the number of jobs "))

jobs = []
print("Enter start time ,finish time,weight ")

for i in range(n):
    s,f,w = map(int,input().split())
    jobs.append([s,f,w])

M = [0]*(n+1)
selected = []
maxProfit = weightSche(jobs)
selection(len(jobs))
print("The maximum profit is ",maxProfit)
print("The selected jobs are ",selected)

