# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        '''
        层次遍历，记录每个节点的深度和位置，当深度改变时，记为该层的最左节点，
        再对于该层次的所有节点，以此计算宽度并保存最大宽度
        '''
        # root node, depth, position
        queue = [(root, 0, 0)]
        cur_depth = left = max_width = 0

        for node, depth, position in queue:
            if node:
                queue.append((node.left, depth + 1, position * 2))
                queue.append((node.right, depth + 1, position * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = position
                max_width = max(position - left + 1, max_width)

        return max_width




