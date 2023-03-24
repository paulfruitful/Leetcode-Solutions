class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        array=[]
        fList=list1
        sList=list2
        while fList:
            array.append(fList.val)
            fList=fList.next
        while sList:
            array.append(sList.val)
            sList=sList.next
        array.sort()
        current=dummy=ListNode()
        for i in array:
            current.next=ListNode(i)
            current=current.next
        return dummy.next 
