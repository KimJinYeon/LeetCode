# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def extract_number(self, target: Optional[ListNode]):
        stringified = ""
        while target.next is not None:
            stringified = str(target.val) + stringified
            target = target.next
        else:
            stringified = str(target.val) + stringified
        return int(stringified)
    
    def to_node(self, target: str):
        base = ListNode(val=target[0])
        current = base
        for char in target[1:]:
            next_node = ListNode()
            next_node.val = int(char)
            next_node.next = current
            current = next_node
        return current
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_l1 = self.extract_number(l1)
        num_l2 = self.extract_number(l2)
        num_sum_str = str(num_l1 + num_l2)
        num_listnode = self.to_node(num_sum_str)
        return num_listnode
        