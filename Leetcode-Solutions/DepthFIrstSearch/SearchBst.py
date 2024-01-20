class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while not root == None:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left  # Fix this line to update the left subtree
            else:
                return root

        return None  # Return None if the value is not found in the binary search tree
