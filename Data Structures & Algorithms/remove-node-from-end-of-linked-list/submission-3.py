# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # the dummy node makes the special case of head removal simple
        dummy = ListNode(next=head)
        left = dummy
        right = dummy

        # we walk the fast pointer ahead so that we have a gap of 'n'
        # between fast and slow pointers
        for _ in range(n+1):
            right = right.next
            n -= 1
        
        # while the fast pointer is valid, we iterate both pointers
        # once fast reaches the end, slow will be the node directly before
        # the node to be removed
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next

        # we return dummy.next because we might have removed the original head
        # if that is what the value of 'n' specified.
        return dummy.next

