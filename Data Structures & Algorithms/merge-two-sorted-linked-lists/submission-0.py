# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while list1 and list2: 
            if list1.val < list2.val:#if value less make dummy node next l1
                node.next = list1 #this makes node next l1
                list1 = list1.next #this makes l1 go to the next element
            else: #if less than or equal do this
                node.next = list2 #copy by do for l2
                list2 = list2.next
            node = node.next #finally transition to next node
        node.next = list1 or list2 #when one is empty link the rest of the non-empty to the node
        return dummy.next #return the our dummy with the new order of nodes