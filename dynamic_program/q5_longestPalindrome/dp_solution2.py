class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        max_l = -1
        start = -1
        for l in range(0,len(s)):
            for i in range(len(s)-l):
                if l==0:
                    dp[i][i+l] = True
                elif l==1:
                    dp[i][i+l] = s[i]==s[i+l]
                else:
                    dp[i][i+l] = dp[i+1][i+l-1] and s[i]==s[i+l]

                if dp[i][i+l] and l>max_l:
                    max_l = l
                    start = i
        return s[start:start+max_l+1]