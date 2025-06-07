#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
from typing import List

from list.ListNode import ListNode
from tree.TreeNode import TreeNode


class ReSolution1:
    # 100
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    # 99. Recover Binary Search Tree
    # 利用sortByOneSwap中的思路
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node1, node2 = None, None
        prev = None

        def search_reversed_node(root):
            if root:
                search_reversed_node(root.left)
                nonlocal prev, node1, node2
                if prev and prev.val > root.val:
                    if not node1:
                        node1 = prev
                if node1 and root.val > node1.val:
                    node2 = prev
                prev = root
                search_reversed_node(root.right)

        search_reversed_node(root)
        if not node2:
            node2 = prev
        # just swap value of node
        node1.val, node2.val = node2.val, node1.val

    # 98. Validate Binary Search Tree
    # 中序遍历判断，使用非递归中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur, prev = root, None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev and prev.val >= cur.val:
                return False
            prev = cur
            cur = cur.right
        return True

    # 97. Interleaving String
    # 1.暴力递归
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def _f(s1: str, i1: int, s2: str, i2: int, s3: str, cur: str):
            if i1 == len(s1) and i2 == len(s2) and cur == s3:
                return True
            ans = False
            if i1 < len(s1):
                ans = ans or _f(s1, i1 + 1, s2, i2, s3, cur + s1[i1])
            if i2 < len(s2):
                ans = ans or _f(s1, i1, s2, i2 + 1, s3, cur + s2[i2])
            return ans

        return _f(s1, 0, s2, 0, s3, "")

    # 2.暴力递归+剪枝
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        def _f(s1: str, i1: int, s2: str, i2: int, s3: str):
            if i1 == len(s1) and i2 == len(s2):
                return True
            ans = False
            if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                ans = ans or _f(s1, i1 + 1, s2, i2, s3)
            if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                ans = ans or _f(s1, i1, s2, i2 + 1, s3)
            return ans

        if len(s1) + len(s2) == len(s3):
            return _f(s1, 0, s2, 0, s3)
        return False

    # 3.剪枝+记忆化
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        memo = [[-1 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

        def _f(s1: str, i1: int, s2: str, i2: int, s3: str):
            if memo[i1][i2] == -1:
                if i1 == len(s1) and i2 == len(s2):
                    memo[i1][i2] = 1
                else:
                    ans = False
                    if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                        ans = ans or _f(s1, i1 + 1, s2, i2, s3)
                    if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                        ans = ans or _f(s1, i1, s2, i2 + 1, s3)
                    memo[i1][i2] = 1 if ans else 0
            return memo[i1][i2] == 1

        if len(s1) + len(s2) == len(s3):
            return _f(s1, 0, s2, 0, s3)
        return False

    # 4.自底向上，动态规划
    # f(i,j)=true表示 s1[i:],s2[j:] 是 s3[i+j:]的interleave
    # f(i,j)= True [i==len(s1) and j==len(s2)]
    # f(i,j)= f(i+1,j) [i<len(s1) and s1[i]==s3[i+j]]
    #        or f(i,j+1) [j<len(s2) and s2[j]==s3[i+j]]
    def isInterleave4(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        n, m = len(s1), len(s2)
        memo = [[False for j in range(m + 1)] for i in range(n + 1)]
        memo[n][m] = True
        # init last row
        for j in range(m - 1, -1, -1):
            if s2[j] == s3[n + j] and memo[n][j + 1]:
                memo[n][j] = True
        # init last col
        for i in range(n - 1, -1, -1):
            if s1[i] == s3[i + m] and memo[i + 1][m]:
                memo[i][m] = True
        # init memo
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s3[i + j] and memo[i + 1][j]:
                    memo[i][j] = True
                elif s2[j] == s3[i + j] and memo[i][j + 1]:
                    memo[i][j] = True
        return memo[0][0]

    # 96
    def numTrees(self, n: int) -> int:
        """
        计算从1...n能组成多少个不同的bst
        f(0)=1
        f(1)=1,
        f(2)=f(0)*f(1)+f(1)*f(0) （选1为根，则左边有0个节点，右边有1个节点，选2为根，则左边有1个节点，右边有0个节点）
        :param n:
        :return:
        """
        memo = [0] * (n + 1)
        memo[0], memo[1] = 1, 1
        for m in range(2, n + 1, 1):
            for i in range(1, m + 1, 1):
                memo[m] += memo[i - 1] * memo[m - i]
        return memo[n]

    # 95
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        96的扩展，将bst构建出来
        :param n:
        :return:
        """

        def _generateTrees(l: int, r: int) -> List[TreeNode]:
            res = []
            if l > r:
                res.append(None)
            elif l == r:
                res.append(TreeNode(l))
            else:
                for i in range(l, r + 1, 1):
                    left_nodes = _generateTrees(l, i - 1)
                    right_nodes = _generateTrees(i + 1, r)
                    for left_node in left_nodes:
                        for right_node in right_nodes:
                            root = TreeNode(i)
                            root.left = left_node
                            root.right = right_node
                            res.append(root)
            return res

        if n > 0:
            return _generateTrees(1, n)
        else:
            return []

    # 94
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        非递归中序遍历二叉树，不算难
        :param root:
        :return:
        """
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # access
            res.append(cur.val)
            cur = cur.right
        return res

    # 93
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        backtracking
        """
        res = []
        one_ip = []

        def _search(s: str):
            nonlocal res, one_ip
            if len(one_ip) == 4:
                if len(s) == 0:
                    res.append(".".join(one_ip))
            else:
                for len1 in range(1, min(3, len(s)) + 1, 1):
                    part = s[:len1]
                    if len1 < 3 or int(part) <= 255:
                        one_ip.append(part)
                        _search(s[len1:])
                        one_ip.pop()

        _search(s)
        return res

    # 92
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        旋转部分链表,指针操作比较复杂
        :param head:
        :param m: 从1开始
        :param n:
        :return:
        """
        i = 1
        cur, prev = head, None
        last = None
        p1, p2 = None, None
        c1, c2 = None, None
        while cur:
            if m == i:
                p1 = prev
                c1 = cur
                last = cur
            if n == i:
                p2 = cur.next
                c2 = cur
            if i > m and i <= n:
                next = cur.next
                cur.next = last
                last = cur
                cur = next
            else:
                prev = cur
                cur = cur.next
            i += 1

        c1.next = None
        if p1:
            p1.next = c2
        if p2:
            c1.next = p2
        if not p1:
            # 从最左边开始翻转，此时不能返回head
            return c2
        return head

    # 91. Decode Ways
    def numDecodings(self, s: str) -> int:
        """
        回溯,dp
        :param s:
        :return:
        """
        n = len(s)
        if n == 0:
            return 0
        memo = [0] * (n + 1)
        memo[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                memo[i] = 0
            else:
                memo[i] += memo[i + 1]
                if i + 1 < n:
                    num = int(s[i:i + 2])
                    if 1 <= num <= 26:
                        memo[i] += memo[i + 2]
        return memo[0]

    # 90. Subsets II
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        排列组合问题，跳过
        :param nums:
        :return:
        """
        pass

    # 89. Gray Code
    def grayCode(self, n: int) -> List[int]:
        """
        n个bit共有2^n个可能，这n个节点组成一张图，每个节点都有n条边
        这个图是连通图，进行一次dfs即可找到一个解
        :param n:
        :return:
        """
        res = []
        visited, stk = set(), []
        start = 0
        stk.append(start)
        while stk:
            cur = stk.pop()
            if not (cur in visited):
                res.append(cur)
                visited.add(cur)
                # 遍历所有邻节点, 111^010=101
                for i in range(0, n):
                    neighbor = cur ^ (1 << i)
                    if not (neighbor in visited):
                        stk.append(neighbor)
        return res

    def grayCode2(self, n: int) -> List[int]:
        """
        n个bit共有2^n个可能，这n个节点组成一张图，每个节点都有n条边
        这个图是连通图，进行一次dfs即可找到一个解
        :param n:
        :return:
        """
        res = []
        visited, stk = set(), []
        start = 0
        stk.append(start)
        visited.add(start)
        while stk:
            cur = stk.pop()
            res.append(cur)
            # 遍历所有邻节点, 111^010=101
            for i in range(0, n):
                neighbor = cur ^ (1 << i)
                if not (neighbor in visited):
                    stk.append(neighbor)
                    visited.add(neighbor)
        return res

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        p1, p2 = m - 1, n - 1
        while p2 >= 0 and p1 >= 0:
            a, b = nums1[p1], nums2[p2]
            if a <= b:
                nums1[i] = b
                p2 -= 1
            else:
                nums1[i] = a
                p1 -= 1
            i -= 1
        while p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1

    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        tow pointer
        :param head:
        :param x:
        :return:
        """
        gtHead = ListNode(-1)
        gtCur = gtHead
        cur = head
        while cur:
            if cur.val >= x:
                gtCur.next = cur
                gtCur = gtCur.next
                cur = cur.next
            else:
                last = cur
                cur = cur.next
        gtCur.next = None
        last.next = gtHead.next
        return head

    # 85

    # 83. Remove Duplicates from Sorted List
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        last, cur = head, head.next
        while cur:
            if last.val != cur.val:
                last.next = cur
                last = cur
            cur = cur.next
        last.next = None
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        # assert head!=null
        if not head or not head.next:
            return head
        else:
            if head.val == head.next.val:
                return self.deleteDuplicates2(head.next)
            else:
                head.next = self.deleteDuplicates2(head.next)
                return head

    # 82. Remove Duplicates from Sorted List II
    def deleteDuplicatese3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dh=ListNode(-1)
        curNew=dh
        cur=head
        while cur:
            if not cur.next or cur.next.val!=cur.val:
                curNew.next=cur
                curNew=curNew.next
                cur=cur.next
            else:
                value=cur.val
                while cur and cur.val==value:
                    cur=cur.next
        curNew.next=None
        return dh.next

    #81. Search in Rotated Sorted Array II
    def search(self, nums: List[int], target: int) -> int:
        """
        不变式：target在nums[l,r]中，l<=r
        :param nums:
        :param target:
        :return:
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if target==nums[m]:
                return m
            if m-1>=l and nums[l]<=nums[m-1]:
                #left part is sorted
                if nums[l]<=target<=nums[m-1]:
                    r=m-1
                else:
                    l=m+1
            else:
                #right part is sorted
                if m+1<=r and nums[m+1]<=target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1


