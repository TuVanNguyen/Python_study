from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        if left == 1:
            tail = head.next
            tail_distance = right-2
            while tail.next and tail_distance > 0:
                tail = tail.next
                tail_distance -= 1
            after_tail = tail.next
            tail.next = None
            nextNode = self.reverseBetween(head.next, left, right - 1)
            tail = nextNode
            while tail.next:
                tail = tail.next
            tail.next = head
            head.next = after_tail
            head = nextNode
        else:
            head.next = self.reverseBetween(head.next, left-1, right-1)
        return head