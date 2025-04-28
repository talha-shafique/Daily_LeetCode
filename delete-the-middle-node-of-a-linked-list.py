# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head
        p2=head
        curr=head
        prev=None
        if curr.next is None:
            return None
        while p2 and p2.next:
            prev=p1
            print('prev',prev.val); p1=p1.next
            print('p1',p1.val); p2=p2.next.next
        prev.next=p1.next
        return curr
        

        
    


        # curr=head
        # prev=None
        # while curr:
        #     if curr.val==
        #     curr.val
        #     prev=curr
        #     curr=curr.next
        
        

        
        

        

        