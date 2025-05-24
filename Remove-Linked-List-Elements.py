# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=head
        prev=None
        stack=[]
        while curr:
            while stack and stack[-1]==val:
                stack.pop()
            stack.append(curr.val)
            curr=curr.next
        if stack and stack[-1]==val:
            stack.pop()
        dummy=ListNode()
        curr=dummy
        for val in stack:
            curr.next=ListNode(val)
            curr=curr.next
        return dummy.next
        