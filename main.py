# Find the Level order of a binary tree and return an array per level
import queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None
        self.elements = 0

    def add(self, value):
        ''' Add values to the tree but skip duplicates'''
        node = Node(value)

        if self.root == None:
            self.root = node
            self.elements += 1

        else:
            current = self.root

            while (current):
                parent = current

                if current.data > value:
                    current = current.left

                    if current is None:
                        parent.left = node
                        return

                elif current.data < value:
                    current = current.right

                    if current is None:
                        parent.right = node
                        return

                elif current.data == value:
                    print("Unable to add element as duplicates are not allowed")
                    return

    def level_order(self, root):
        '''This method retrieves the level order of the current BinaryTree'''
        # If the tree is empty return an empty array as result
        if self.root is None:
            return []

        # Holds the resulting list with level ordered items
        result = []
        # Queue that holds all the nodes in each level
        q = queue.Queue()
        # Add the root to the queue
        q.put(root)
        # While there are nodes in the queue
        while q.empty() is not True:
            # The numebr of items in the queue
            length = q.qsize()
            # The count of how many items have been popped from the queue
            count = 0
            # list that holds the values per level
            current_vals = []

            # While there are nodes in the queue
            while count < length:
                # Get the node from the queue
                current_node = q.get()
                # Save its current value and add it to the placeholder list
                current_vals.append(current_node.data)

                # If there are nodes to the left or right, add them to the queue
                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)

                # Increase the count
                count += 1

            # Add the items in the current level to the results list
            result.append(current_vals)

        return result


__name__ = "__main__"

bt = BinaryTree()
bt.add(50)
bt.add(41)
bt.add(10)
bt.add(30)
bt.add(25)
bt.add(6)
bt.add(7)
bt.add(69)

print(bt.level_order(bt.root))
