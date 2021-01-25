# 정렬되어있는 두 연결 리스트를 합쳐라
# 입력 1->2->4, 1->3->4
# 출력 1->1->2->3->4->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    # 우선순위 >, not, and, or
    if (not l1) or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1

    if l1:
        l1.next = merge_two_list(l1.next, l2)

    return l1


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = merge_two_list(l1, l2)
