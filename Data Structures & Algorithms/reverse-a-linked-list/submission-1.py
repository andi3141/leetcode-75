# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        node = head

        nodeList = [head]
        while node.next is not None:
            node = node.next
            nodeList.append(node)

        # reset next nodes
        for node in nodeList:
            node.next = None

        for i in range(len(nodeList) - 1, 0, -1):
            nodeList[i].next = nodeList[i - 1]
        return nodeList[-1]
