"""
找到树的最小深度
ps: 针对树的节点进行迭代, 遇到的首个不存在子节点的节点所在层级, 就是树的最小深度
"""
import unittest
from collections import deque

from tree import TreeNode


def recur_min_depth(root: TreeNode):
    """
    找到树的最小层级
    该处可以对比找到树的最大层级的代码, 不同的是
    min_deep(root) = min(min_deep(root.left), min_deep(root.right)) + 1
    :param root:
    :return:
    """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    # if root.left is not None and root.right is not None:
    #     left_min_deep = recur_min_depth(root.left)
    #     right_min_deep = recur_min_depth(root.right)
    #     return min(left_min_deep, right_min_deep) + 1
    # elif root.left is not None:
    #     left_min_deep = recur_min_depth(root.left)
    #     return left_min_deep + 1
    # elif root.right is not None:
    #     right_min_deep = recur_min_depth(root.right)
    #     return right_min_deep + 1
    # else:
    #     return 1
    # 如果, 当前层级下方有节点了, 那么当前节点的层级就至少为2了, 所以该处有 max(min_deep, 1) 这种操作
    left_min_deep = recur_min_depth(root.left)
    right_min_deep = recur_min_depth(root.right)
    return max(min(left_min_deep, right_min_deep), 1) + 1


# iterative
def min_height_bfs(root):
    """
    bfs获取树的最小深度
    :param root:
    :return:
    """
    if root is None:
        return 0
    height = 0
    level = [root]
    while level:
        height += 1
        new_level = []
        # 迭代当前的层级
        for node in level:
            if node.left is None and node.right is None:
                # 当前层级中, 存在节点没有子节点, 那么当前层级高度就是最小的
                return height
            if node.left is not None:
                new_level.append(node.left)
            if node.right is not None:
                new_level.append(node.right)
        # 走到下一层级
        level = new_level
    return height


def min_depth(root):
    if not root:
        return 0
    queue = deque([(root, 1)])  # 将根节点和深度初始化为1放入队列
    while queue:
        node, depth = queue.popleft()  # 从队列中取出节点和对应的深度
        if not node.left and not node.right:  # 判断是否为叶子节点
            return depth  # 返回最小深度
        if node.left:
            queue.append((node.left, depth + 1))  # 左子树入队，深度加1
        if node.right:
            queue.append((node.right, depth + 1))  # 右子树入队，深度加1


def min_height_dfs(root) -> int:
    """
    使用dfs获取树的最小深度, 感觉方案并不合适, 这种方式需要迭代整棵树
    :param root:
    :return:
    """
    if root is None:
        return 0
    heights = None
    stack = [(root, 1)]
    while stack:
        node, level = stack.pop()
        if node.right is not None:
            stack.append((node.right, level + 1))
        if node.left is not None:
            stack.append((node.left, level + 1))
        if node.left is None and node.right is None:
            if heights is None:
                heights = level
            else:
                heights = min(heights, level)

    return heights


class TestMinHeight(unittest.TestCase):
    """
        10
        |\
       12 15
       |\  |
    25  30 36
      \
      100
    """

    def setUp(self):
        self.tree = TreeNode(10)
        self.tree.left = TreeNode(12)
        self.tree.right = TreeNode(15)
        self.tree.left.left = TreeNode(25)
        self.tree.left.left.right = TreeNode(100)
        self.tree.left.right = TreeNode(30)
        self.tree.right.left = TreeNode(36)

    def test_min_height_bfs(self):
        self.assertEqual(min_height_bfs(self.tree), 3)

    def test_min_height_dfs(self):
        self.assertEqual(min_height_dfs(self.tree), 3)

    def test_recur_min_depth(self):
        self.assertEqual(recur_min_depth(self.tree), 3)


if __name__ == '__main__':
    unittest.main()
