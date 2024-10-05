"""
Your task is to count the number of ways to construct sum n by throwing a dice one or more times. Each throw produces an outcome between 1 and  6.
For example, if n=3, there are 4 ways:

1+1+1
1+2
2+1
3

Input
The only input line has an integer n.
Output
Print the number of ways modulo 10^9+7.
Constraints

1 \le n \le 10^6

Example
Input:
3

Output:
4
"""
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


    
 

n=int(input())
dp=[0]*(n+1)

dp[0]=1
mod=1000000007



for i in range(1,n+1):
    for j in range(1,7):
        if(i-j>=0):
            dp[i]=(dp[i]+dp[i-j])%mod



print(dp[n])

    

