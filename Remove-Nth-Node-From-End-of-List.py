# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        count=0
        curr=head
        prev=None
        while curr:
            curr=curr.next
            length+=1
        tar=(length-n)+1
        curr=head
        while curr is not None:
            count+=1
            if count==tar:
                if prev is None:
                    head=curr.next
                else:
                    prev.next=curr.next
                break
            prev=curr
            curr=curr.next
        return head
        
        