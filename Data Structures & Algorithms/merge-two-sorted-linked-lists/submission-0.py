# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        list3 = ListNode(val=0, next=None)

        node3 = list3
        node1 = list1
        node2 = list2

        while 1 == 1:
            if node1 is None and node2 is None:
                return list3.next

            if node2 is None:
                node3.next = node1
                node3 = node1
                node1 = node1.next
            elif node1 is None:
                node3.next = node2
                node3 = node2
                node2 = node2.next
            elif node1.val <= node2.val:
                node3.next = node1
                node3 = node1
                node1 = node1.next
            else:
                node3.next = node2
                node3 = node2
                node2 = node2.next

