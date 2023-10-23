"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""

import unittest

from tree import TreeNode


def max_height_with_bfs(root: TreeNode):
    """
    打印树的最大层级
    由于广度优先，是按树的层级进行遍历的，在该处直接有树的层级，所以不需要保存level字段
    :param root:
    :return:
    """
    if root is None:
        return 0
    height = 0
    queue = [root]
    while queue:
        height += 1
        level = []
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)
        queue = level
    return height


def max_height_with_dfs(root: TreeNode):
    """
    进行深度优先遍历时候，由于树的层级没有保存，在该处，需要添加一个字段来保存遍历的当前节点的深度
    :param root:
    :return:
    """
    if not root:
        return 0
    travel_stack = [(root, 1)]
    height = 1
    while travel_stack:
        node, level = travel_stack.pop()
        height = max(height, level)
        if node.right:
            travel_stack.append((node.right, level + 1))
        if node.left:
            travel_stack.append((node.left, level + 1))
    return height


def recur_max_height_with(root: TreeNode):
    """
    使用递归来计算树的最大深度
    deep(root) = 1 + max(deep(root.left), deep(root.right))
    :param root:
    :return:
    """
    if not root:
        return 0
    max_left = recur_max_height_with(root.left)
    max_right = recur_max_height_with(root.right)
    return max(max_left, max_right) + 1


def recur_print_tree(root):
    """
    打印树的结构，一般使用递归，下面的是使用 中-> 左-> 右 的顺序来打印树的节点新
        root
        | \
    left   right
    :param root:
    :return:
    """
    if root is None:
        return
    print(root.val)
    recur_print_tree(root.left)
    recur_print_tree(root.right)


class TestMaxHeight(unittest.TestCase):
    def test_max_height(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(max_height_with_bfs(root), 3)
        self.assertEqual(max_height_with_dfs(root), 3)
        self.assertEqual(recur_max_height_with(root), 3)
        recur_print_tree(root)


if __name__ == '__main__':
    unittest.main()
