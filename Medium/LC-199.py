# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# Binary Tree Right Side View
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode):
        d = defaultdict(list)
        def dfs(node, h):
            if not node: return 
            d[h].append(node.val)
            dfs(node.left,h+1)
            dfs(node.right, h + 1)
        dfs(root, 0)
        return [v[-1] for k,v in sorted(d.items())]