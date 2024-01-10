
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res=[]
        queue=list([root])

        while queue:
            level_length=len(queue)

            for i in range(level_length):
                node=queue.pop(0)

                if i == level_length-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res





