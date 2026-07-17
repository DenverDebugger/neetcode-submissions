# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        if count == n:
            return head.next
            
        curr = head
        curr_count = 0

        while curr and curr_count < (count - n - 1):
            curr = curr.next
            curr_count += 1

        if curr.next:
            curr.next = curr.next.next
        
        return head
