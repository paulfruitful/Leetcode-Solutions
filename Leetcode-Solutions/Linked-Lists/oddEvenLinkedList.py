# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
       if head: 

        even=head.next
        odd=head
        evenHead=even


        while even and even.next:
            odd.next=even.next
            odd=odd.next

            even.next=odd.next 
            even=even.next

        odd.next=evenHead
        return head 
       return head
