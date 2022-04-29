
from typing import List


class Solution:


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.flag = False
        m, n = len(board), len(board[0])
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def legal_path(i, j):
            if (i >= 0 and i < m) and (j >= 0 and j < n):
                return True
            return False

        def dfs(remain, visited, i, j):

            if len(remain) == 0:
                self.flag = True
                return
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                if legal_path(ni, nj) and ((ni, nj) not in visited) and remain[0] == board[ni][nj]:
                    # visited.add((ni, nj))
                    new_vis = set()
                    new_vis.add((ni, nj))
                    new_vis = new_vis | visited
                    dfs(remain[1:], new_vis, ni, nj)

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    dfs(word[1:], visited, i, j)

        return self.flag

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    s = Solution().exist(board,word)
    print(s)
