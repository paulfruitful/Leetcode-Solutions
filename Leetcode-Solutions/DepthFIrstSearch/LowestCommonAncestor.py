
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
   
        if root==None or root==p or root==q:
            return root
        
        right=self.lowestCommonAncestor( root.right, p, q)
        left=self.lowestCommonAncestor( root.left, p, q)
        if right and left:
            return root
        
        return right or left
