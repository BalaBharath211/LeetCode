# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightside(self,root,level,ds):
        if root is None:
            return
        if len(ds)==level:
            ds.append(root.val)
        self.rightside(root.right,level+1,ds)
        self.rightside(root.left,level+1,ds)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds=[]
        self.rightside(root,0,ds)
        return ds