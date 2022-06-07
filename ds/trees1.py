# BST

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root

def search(root,key):
    if root is None:
        return False
    else:
        if key == root.data:
            return root.data
        if key < root.data:
            return search(root.left,key)
        else:
            return search(root.right,key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# Level order traversal of tree
def level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while (len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def minValueNode(root):
    index = root
    while index.left is not None:
        index = index.left
    return index

def deleteNode(root,key):
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left,key)
    if key > root.data:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

        return root


r = Node(50)
insert(r,30)
insert(r,20)
insert(r,40)
insert(r,70)
insert(r,60)
insert(r,80)
# deleteNode(r,20)
# inorder(r)
# deleteNode(r,30)
# deleteNode(r,50)
# print(minValueNode(r))
# level_order(r)
# inorder(r)
# print(search(r,40))

