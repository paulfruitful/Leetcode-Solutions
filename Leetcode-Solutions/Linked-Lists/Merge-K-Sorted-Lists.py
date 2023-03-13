# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next):
#         self.val = val
#         self.next = next

        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        linkedList=[]
        
        for i in range(0,len(lists)):
           num=lists[i]
           while num:
              linkedList.append(num.val)
              num=num.next
        linkedList.sort()
        sorter=ListNode(0)
        sorting=sorter
        for i in linkedList:
           sorting.next = ListNode(val=i)
           sorting=sorting.next
        
        return sorter.next
