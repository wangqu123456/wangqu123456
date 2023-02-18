class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res_list = []
        while head != None:
            # print(head.val)
            res_list.append(head.val)
            # print(res_list)
            head = head.next
        res_list.reverse()
        return res_list

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(2)
node1.next = node2
node2.next = node3

sol = Solution()
print(sol.reversePrint(node1))
