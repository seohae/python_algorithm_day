# 연결리스트가 팰린드롬인지 체크 (팰린드롬이란, 거꾸로해도 같은 문자)

# 입력 1-> 2 : false
# 입력 1->2->2->1 : true
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 리스트 변환
def isPalindrome(self, head:ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬인지 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


