"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(node,parent,left):
            if node:
                if parent:
                    if left:
                        node.next=parent.right
                    else:
                        if parent.next:
                            node.next=parent.next.left
                dfs(node.left,node,True)
                dfs(node.right,node,False)
        dfs(root,None, False)
        return root
