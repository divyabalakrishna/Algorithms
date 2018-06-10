
import queue
class Node:
    def __init__(self, value='0'):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, value):
        self.left = Node(value)

    def add_right(self, value):
        self.right = Node(value)

    def _confirm_dup_st(self, root1, root2):
        if (root1.left is None and root2.left is None and
           root1.right is None and root2.right is None):
            return False

        q1 = queue.Queue(0)
        q1.put(root1)
        q2 = queue.Queue(0)
        q2.put(root2)
        while q1.qsize() > 0 and q2.qsize() > 0:
            temp1 = q1.get()
            temp2 = q2.get()
            if temp1.value != temp2.value:
                return False

            if temp1.left is not None:
                q1.put(temp1.left)
            if temp1.right is not None:
                q1.put(temp1.right)
            if temp2.left is not None:
                q2.put(temp2.left)
            if temp2.right is not None:
                q2.put(temp2.right)

        return True

    def _get_st_node(self, root, visited):
        for node in visited:
            if root.value == node.value:
                return node
        return -1

    def dup_st(self):
        q = queue.Queue(0)
        q.put(self)
        visited = []
        while q.qsize() > 0:
            temp = q.get()
            st_root = self._get_st_node(temp, visited)
            if st_root != -1:
                break
            visited.append(temp)
            if temp.left is not None:
                q.put(temp.left)
            if temp.right is not None:
                q.put(temp.right)
            q.task_done()

        if temp.value != st_root.value:
            return False
        return self._confirm_dup_st(temp, st_root)

root = Node('A')
root.add_left('B')
root.add_right('C')
root.left.add_left('D')
root.left.add_right('E')
root.right.add_right('B')
root.right.right.add_left('Q')
root.right.right.add_right('E')
print(root.dup_st())
