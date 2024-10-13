import sys
sys.stdout = open('DynamicPrograming/output.txt', 'w')
sys.stdin = open('DynamicPrograming/input.txt', 'r')


"""Question"""
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""

"""Recursive Solution
def climbStairs(n):
    if n<=0 or n==1:
        return 1
    return climbStairs(n-1)+climbStairs(n-2)
"""


"""Memorization
def help(n,dp):
    if n<=0 or n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]
    
    dp[n]=help(n-1,dp)+help(n-2,dp)
    return dp[n]"""


"""Tebulation"""

if __name__=="__main__":
    n=int(input())
    dp=[-1]*(n+1)
    dp[0]=1
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

        
    print(dp[n]))