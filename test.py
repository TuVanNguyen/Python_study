from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    last_node = None
    min_diff = float("inf")
    def dfs(root: Optional[TreeNode]):
        nonlocal last_node
        nonlocal min_diff
        if root == None:
            return
        dfs(root.left)
        if last_node:
            min_diff = min(min_diff, root.val- last_node.val)
        last_node = root
        dfs(root.right)
        
    dfs(root)
    return min_diff




