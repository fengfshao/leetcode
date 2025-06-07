from collections import deque


class Node:
    data = ""
    neighbors = []

    def __init__(self, data, neighbors=None) -> None:
        if neighbors is None:
            neighbors = []
        self.data = data
        self.neighbors = neighbors


def access(cur: Node):
    print(cur.data)


# 递归版
def search_re(cur: Node):
    visisted = set()

    def _search(cur: Node):
        nonlocal visisted
        access(cur)
        visisted.add(cur)
        for neighbor in cur.neighbors:
            if neighbor not in visisted:
                _search(neighbor)

    _search(cur)

#迭代版
def search_it(cur: Node):
    visisted = set()
    stack = []
    stack.append(cur)
    while stack:
        cur = stack.pop()
        if cur not in visisted:
            access(cur)
            visisted.add(cur)
            for neighbor in cur.neighbors:
                if neighbor not in visisted:
                    stack.append(neighbor)


def bfs(cur: Node):
    visisted = set()
    queue = deque()
    queue.append(cur)
    while queue:
        cur = queue.popleft()
        if cur not in visisted:
            access(cur)
            visisted.add(cur)
            for neighbor in cur.neighbors:
                if neighbor not in visisted:
                    queue.append(neighbor)


if __name__ == '__main__':
    # 构建graph
    # a- b - d
    #  \ |  |
    #   c - e

    a, b, c, d, e = Node("a"), Node("b"), Node("c"), Node("d"), Node("e")
    a.neighbors.extend([b, c])
    b.neighbors.extend([a, c, d])
    c.neighbors.extend([a, b, e])
    d.neighbors.extend([b, e])
    e.neighbors.extend([c, d])

    # search_it(a)  # a c e d b
    # search_re(a)  # a b c e d
    # bfs(a) # a b c d e