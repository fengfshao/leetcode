from unittest import TestCase

from list.ListUtil import ListUtil
from review1.ReSolution1 import ReSolution1
from tree.TreeUtil import TreeUtil


class TestReSolution1(TestCase):
    def setUp(self) -> None:
        self.sol = ReSolution1()

    def tearDown(self) -> None:
        pass

    def test_num_trees(self):
        n = 3
        res = self.sol.numTrees(n)
        print(res)
        assert res == 5

    def test__generate_trees(self):
        n = 3
        res = self.sol.generateTrees(n)
        for root in res:
            TreeUtil.printTree(root)

    def test_inorder_traversal(self):
        root = TreeUtil.mkTreeByPreorder([1, -1, 2, 3, -1, -1, -1])
        TreeUtil.printTree(root)
        print(self.sol.inorderTraversal(root))

    def test_restore_ip_addresses(self):
        input = "25525511135"
        res = self.sol.restoreIpAddresses(input)
        print(res)

    def test_reverse_between(self):
        head = ListUtil.mkList([1, 2, 3, 4, 5])
        nh = self.sol.reverseBetween(head, 2, 2)
        ListUtil.printList(nh)

    def test_num_decodings(self):
        s = "1010"
        res = self.sol.numDecodings(s)
        print(res)

    def test_gray_code(self):
        n = 2
        res = self.sol.grayCode2(3)
        print(res)

    def test_merge(self):
        a = [0, 4, 5, 0, 0, 0]
        b = [1, 2, 6]
        self.sol.merge(a, 3, b, 3)
        print(a)

    def test_partition(self):
        head = ListUtil.mkList([1, 2, 4, 5, 3, 6])
        ListUtil.printList(head)

        newHead = self.sol.partition(head, 3)
        ListUtil.printList(newHead)

    def test_delete_duplicates(self):
        head = ListUtil.mkList([1, 1, 2, 3, 3, 4, 4])
        newHead = self.sol.deleteDuplicatese3(head)
        ListUtil.printList(newHead)

    def test_search(self):
        arr = [1]
        assert -1 == self.sol.search(arr, 0)
        arr = [1]
        assert 0 == self.sol.search(arr, 1)
        arr = [1,2]
        assert 0 == self.sol.search(arr, 1)
        arr = [2,1]
        assert -1 == self.sol.search(arr, 3)
        arr = [3,1,2]
        assert -1 == self.sol.search(arr, 4)
        assert 0 == self.sol.search(arr, 3)
        arr = [7,8,1,2,3,4,5]
        assert 2 == self.sol.search(arr, 1)


