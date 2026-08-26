# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderTravers(self,root,arr):
        if root is None:
            return 
        arr.append(root.val)
        self.preOrderTravers(root.left,arr)
        self.preOrderTravers(root.right,arr)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr=[]
        self.preOrderTravers(root,arr)
        return arr