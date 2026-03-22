class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right,key)


def delete(root, key):
    if not root:
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# TEST
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("\nBST Inorder (Sorted):")
inorder(root)

print("\nSearch 40:", "Found" if search(root, 40) else "Not Found")

root = delete(root, 30)
print("After deleting 30:")
inorder(root)
