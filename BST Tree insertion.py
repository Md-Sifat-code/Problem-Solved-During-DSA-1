class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None


def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return  root


root = None
values = [50,30,20,40,70,60,80]
for v in values:
    root = insert(root,v)

