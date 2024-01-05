class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        res = []
        for list_item in lists:
            root = list_item
            while root:
                res.append(root.val)
                root = root.next

        head = point = ListNode(0)

        for x in sorted(res):
            point.next = ListNode(x)
            point = point.next
        return head.next
