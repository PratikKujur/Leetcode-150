import sys
sys.stdout = open('DynamicPrograming/output.txt', 'w')
sys.stdin = open('DynamicPrograming/input.txt', 'r')


"""Question
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12."""

"""Recursive Solution
def help(i,nums):
    if i==0:
        return nums[i]
    if i<0:
        return -1*float('inf')
    
    return max(nums[i]+help(i-2,nums),help(i-1,nums))
"""

    

"""Memorization"""
def help(i,nums,dp):
    if i==0:
        return nums[i]
    if i<0:
        return -1*float('inf')
    
    if dp[i]!=-1:
        return dp[i]
    
    dp[i]=max(nums[i]+help(i-2,nums,dp),help(i-1,nums,dp))

    return dp[i]

"""Tebulation"""

if __name__=="__main__":
    nums=list(map(int,input().split()))
    n = len(nums)
    if n==1:
         print(nums[0])

    dp = [0] * (n + 1)
    dp[0] = nums[0]
    dp[1]=max(nums[0],nums[1])

    for i in range(2, n):
        if i - 2 >= 0 and i - 1 >= 0:
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    
    print(dp[n - 1])
