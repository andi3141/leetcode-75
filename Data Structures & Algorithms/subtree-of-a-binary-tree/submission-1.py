# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        sameLeft = self.isSameTree(p.left, q.left)
        sameRight = self.isSameTree(p.right, q.right)

        return sameLeft and sameRight

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        sameLeft = self.isSubtree(root.left, subRoot)
        sameRight = self.isSubtree(root.right, subRoot)

        return sameLeft or sameRight
        
