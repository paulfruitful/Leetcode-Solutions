class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listed=[]
        num=head
        while num:
            listed.append(num.val)
            num=num.next
        median=len(listed)/2
        values=listed[median:]
        dummy=ListNode()
        current=dummy

        for i in values:
            current.next=ListNode(i)
            current=current.next
        return dummy.next
