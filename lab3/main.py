class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def depths_sum(root: TreeNode) -> int:
    def depth_sum(node, depth):
        if node is None:
            return 0
        return depth + depth_sum(node.left, depth + 1) + depth_sum(node.right, depth + 1)

    return depth_sum(root, 0)


root = TreeNode(10)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(1)
res = depths_sum(root)
print(res)
