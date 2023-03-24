# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        clone=head
        reversed_array=[]
        while clone:
            reversed_array.append(clone.val)
            clone=clone.next
        reversed_array.reverse()
        current=dummy=ListNode()
        for i in reversed_array:
            current.next=ListNode(i)
            current=current.next
        return dummy.next
