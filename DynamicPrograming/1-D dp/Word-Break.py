import sys
sys.stdout = open('DynamicPrograming/output.txt', 'w')
sys.stdin = open('DynamicPrograming/input.txt', 'r')


"""Question
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

"""Recursive Solution
def help(i, s, wordSet):
    if i == len(s):
        return True
    
    temp = ""

    for j in range(i, len(s)):  # Fix: use range instead of a tuple
        temp += s[j]
        if temp in wordSet:
            if help(j + 1, s, wordSet):
                return True

    return False"""

       
    

"""Memorization"""
def help(i, s, wordSet,dp):
    if i == len(s):
        return 1
    
    if dp[i]!=-1:
        return dp[i]
    temp = ""

    for j in range(i, len(s)):  # Fix: use range instead of a tuple
        temp += s[j]
        if temp in wordSet:
            if help(j + 1, s, wordSet,dp):
                dp[j]=1
                return dp[j]

    dp[i]=0
    return dp[i]

"""Tebulation"""

if __name__ == "__main__": 
    s = str(input())
    wordDict = list(map(str, input().split()))
    dp=[-1]*(len(s)+1)
    wordSet = set(wordDict)

  
    dp[len(s)] = 1

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break                    
                

    print(dp[0])