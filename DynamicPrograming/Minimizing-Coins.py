'''
Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to produce a sum of money x using the available coins in such a way that the number of coins is minimal.
For example, if the coins are \{1,5,7\} and the desired sum is 11, an optimal solution is 5+5+1 which requires 3 coins.
Input
The first input line has two integers n and x: the number of coins and the desired sum of money.
The second line has n distinct integers c_1,c_2,\dots,c_n: the value of each coin.
Output
Print one integer: the minimum number of coins. If it is not possible to produce the desired sum, print -1.
Constraints

1 \le n \le 100
1 \le x \le 10^6
1 \le c_i \le 10^6

Example
Input:
3 11
1 5 7

Output:
3
'''
'''
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def mincoins(i,n,target,nums):
    if target==0:
        return 0
    if i<0 or target<0:
        return float('inf')
    
    pick=float('inf')

    if(target-nums[i]>=0):
        pick=1+mincoins(i,n,target-nums[i],nums)
    
    notpick=mincoins(i-1,n,target,nums)

    return min(pick,notpick)
'''

if __name__=="__main__":
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    
    #ans=mincoins(n-1,n,target,nums)
    dp=[[float('inf')]*(target+1) for _ in range(n)]
    
    for i in range(n):
        dp[i][0]=0
    
    for i in range(n):
        pick=float('inf')
        for t in range(target+1):
            if(t-nums[i]>=0):
                pick=1+dp[i][t-nums[i]]
            
            notpick=dp[i-1][t]

            dp[i][t]=min(pick,notpick)
    
    if(dp[n-1][target]==float('inf')):
        print(-1)
    else:
        print(dp[n-1][target])









 
