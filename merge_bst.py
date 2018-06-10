
class Node:
    def __init__(self, value='0'):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node[%s]" % self.value

    def add_left(self, value):
        self.left = Node(value)

    def add_right(self, value):
        self.right = Node(value)

def get_stack(root, list=None):
    # list stores elements in right, root and left order
    if list is None:
        list = []
    if root.right is None and root.left is None:
        list.insert(0, root.value)
        return list

    if root.right is not None:
        list = get_stack(root.right, list)

    list.insert(0, root.value)

    if root.left is not None:
        list = get_stack(root.left, list)

    return list

def merge(root1, root2):
    stack1 = []
    stack2 = []
    if root1 is not None:
        stack1 = get_stack(root1)
    if root2 is not None:
        stack2 = get_stack(root2)
    while len(stack1) > 0 and len(stack2) > 0:
        if stack1[0] > stack2[0]:
            print(stack2[0])
            stack2.remove(stack2[0])
            print(stack1[0])
            stack1.remove(stack1[0])
        else:
            print(stack1[0])
            stack1.remove(stack1[0])
            print(stack2[0])
            stack2.remove(stack2[0])

    while len(stack1) > 0:
        print(stack1[0])
        stack1.remove(stack1[0])

    while len(stack2) > 0:
        print(stack2[0])
        stack2.remove(stack2[0])

root1 = Node(1)
root1.add_right(33)
root1.right.add_left(4)

root2 = Node(6)
root2.add_left(1)
root2.add_right(7)

merge(root1, root2) 
