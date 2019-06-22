#Uses Python3
dp = {}
def lcs(listx, listy, m,n,dp):
    if m == 0 or n == 0:
        return 0
    if listx[m-1] == listy[n-1]:
        if (m,n) in dp:
            return dp[m, n]
        else:
            dp[m, n] = 1 + lcs(listx,listy, m-1, n-1,dp)
            return dp[m, n]
    elif listx[m-1] != listy[n-1]:
        if (m,n) in dp:
            return dp[m, n]
        else:    
            t =  max(lcs(listx,listy, m-1, n,dp), lcs(listx,listy, m, n-1,dp))
            dp[m, n] = t
            return dp[m, n]

x = int(input())
listx = input().split()
y = int(input())
listy = input().split()
print(lcs(listx, listy, x, y,dp))

