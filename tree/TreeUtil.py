from typing import List

from tree.TreeNode import TreeNode


class TreeUtil:
    @classmethod
    def mkTreeByPreorder(cls, arr: List[int]) -> TreeNode:
        return TreeUtil.__mkTreeByPreorder(arr, [0])

    @classmethod
    def __mkTreeByPreorder(cls, arr: List[int], idx_pointer: List[int]) -> TreeNode:
        value = arr[idx_pointer[0]]
        root = None if (value == -1) else TreeNode(value, None, None)
        idx_pointer[0] += 1
        if root:
            root.left = TreeUtil.__mkTreeByPreorder(arr, idx_pointer)
            root.right = TreeUtil.__mkTreeByPreorder(arr, idx_pointer)
        return root

    @classmethod
    def printTree(cls, root: TreeNode):
        res, stk = [], []
        cur = root
        while cur or stk:
            while cur:
                res.append(cur.val)
                stk.append(cur.right)
                cur = cur.left
            cur = stk.pop()
        print(res)


if __name__ == '__main__':
    root = TreeUtil.mkTreeByPreorder([1, 1, 3, -1, -1, -1, 2, -1, -1])
    TreeUtil.printTree(None)
