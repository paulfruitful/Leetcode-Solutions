# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        array=[]
        copy=head
        while copy:
            array.append(copy.val)
            copy=copy.next
        array.pop(-n)
        current=dummy=ListNode()
        for i in array:
            current.next=ListNode(i)
            current=current.next
        return dummy.next
