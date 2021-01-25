# 연결리스트를 뒤집어라

# 1->2->3->4->5->NULL
# 5->4->3->2->1->NULL

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head:ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

