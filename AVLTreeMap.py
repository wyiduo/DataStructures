class BinaryNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None


class AVLTreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        new_node = BinaryNode(key, value)

        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root

            while True:
                if new_node.key <= current_node.key:
                    if current_node.left == None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def get_node_height(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 0

        left_child_height = self.get_node_height(node.left)
        right_child_height = self.get_node_height(node.right)

        if left_child_height >= right_child_height:
            return left_child_height + 1
        else:
            return right_child_height + 1

    def get_helper(self, key, root_node):
        if root_node == None:
            return ""
        else:
            if root_node.key == key:
                return root_node.value

            return self.get_helper(key, root_node.left) \
                   + self.get_helper(key, root_node.right)

    def get(self, key):
        temp = self.get_helper(key, self.root)
        if temp == "":
            return "null"
        else:
            return temp


if __name__ == "__main__":
    test_tree = AVLTreeMap()

    test_tree.put(11, "bob")
    test_tree.put(20, "anna")
    test_tree.put(24, "tom")
    test_tree.put(10, "david")
    test_tree.put(13, "david")
    test_tree.put(7, "ben")
    test_tree.put(30, "karen")
    test_tree.put(36, "erin")
    test_tree.put(25, "david")

    print("test_tree.get(20) = ")
    print(test_tree.get(20))
    print("test_tree.get(36) = ")
    print(test_tree.get(36))
    print("test_tree.get(100) = ")
    print(test_tree.get(100))
