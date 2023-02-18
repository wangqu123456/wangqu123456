class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        tree_len = len(preorder)
        head = getLeftTree(0, tree_len-1, preorder, inorder, 0)
        return head


def getLeftTree(start, end, preorder, inorder, pointer):
    if start > end:
        return None
    if pointer >= len(preorder) or pointer >= end:
        return None
    node = TreeNode(preorder[pointer])
    tmp_index = getIndex(pointer, inorder)
    pointer = pointer + 1
    node.left = getLeftTree(start, tmp_index-1, preorder, inorder, pointer)
    node.right = getLeftTree(tmp_index, end, preorder, inorder, pointer)

    return node


def getIndex(i, inorder):
    return inorder.index(i)
