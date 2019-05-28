class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = node(value)
            else:
                self._insert(value, current_node.right_child)

        else:
            print("value is already in the tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value is current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._search(value, current_node.right_child)

        return False


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree


tree = binary_search_tree()
# tree = fill_tree(tree)

tree.insert(3)
tree.insert(5)
tree.insert(6)
tree.insert(8)
tree.insert(2)
tree.print_tree()

print(f"tree height is {tree.height()}")

print(f"search for number 3 : {tree.search(3)}")
print(f"search for number 10 : {tree.search(10)}")
