class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.isBreak(s, wordDict, 0, len(s))

    def isBreak(self, s, wordDict, i, j):
        """
        判断s[i:j]是否可以拆分
        """
        res = False
        if i >= j:
            return True
        for k in range(i, j):
            if s[i:k+1] in wordDict:
                tmp = self.isBreak(s, wordDict, k+1 , j)
                res = tmp or res

        return res
