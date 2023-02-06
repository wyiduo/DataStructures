class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None # left is less, right is more
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.highest_abs_node_difference = -1

    def insert(self, value):
        new_node = BinaryNode(value)
        
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root

            while True: # iterate through the tree until an empty node
                # is available for the value being inserted into the tree
                if new_node.value <= current_node.value:
                    # go left
                    if current_node.left == None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else: # if new_node.value > current_node.value
                    # go right
                    if current_node.right == None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def get_node_height(self, node):
        if node == None: # used for breaking recursion when the current node
            # only has 1 child node; returns 0 to use the height of the other
            # child node
            return 0

        if node.left == None and node.right == None:
            return 0
        
        left_child_height = self.get_node_height(node.left)
        right_child_height = self.get_node_height(node.right)

        # get greater of the left or right child nodes and return the child
        # node height + 1 to account for the edge being added to the child
        # node to get the current node
        if left_child_height >= right_child_height:
            return left_child_height + 1
        else: # left_child_height < right_child_height
            return right_child_height + 1
        
    def get_total_height_recursive(self, root_node):
        if root_node == None:
            return 0
        elif root_node.left == None and root_node.right == None:
            return 0

        return self.get_total_height_recursive(root_node.left) \
               + self.get_total_height_recursive(root_node.right) \
               + self.get_node_height(root_node)

    def get_total_height(self):
        return self.get_total_height_recursive(self.root)

    def get_number_of_nodes(self, root_node):
        if root_node == None:
            return 0

        return self.get_number_of_nodes(root_node.left) \
               + self.get_number_of_nodes(root_node.right) + 1

    def get_abs_node_difference(self, node): # gets the absolute value of the
        # difference between the number of nodes in the left subtree and the
        # number of nodes in the right subtree
        return abs(self.get_number_of_nodes(node.left) \
                - self.get_number_of_nodes(node.right))

    def get_weight_balance_factor_helper(self, root_node): # recusively iterates
        # through the tree to apply the get_abs_node_difference() function and
        # will set self.highest_abs_node_difference as the highest value returned
        # by get_abs_node_difference() for all values in the tree
        if root_node == None:
            return # return void

        node_difference_current = self.get_abs_node_difference(root_node)

        if node_difference_current > self.highest_abs_node_difference:
            self.highest_abs_node_difference = node_difference_current

        self.get_weight_balance_factor_helper(root_node.left)
        self.get_weight_balance_factor_helper(root_node.right)

    def get_weight_balance_factor(self): # will return self.highest_abs_node_difference
        # after running the get_weight_balance_factor_helper() procedure
        self.highest_abs_node_difference = -1
        
        self.get_weight_balance_factor_helper(self.root)
        temp = self.highest_abs_node_difference
        
        self.highest_abs_node_difference = -1
        return temp

    def serialize_helper(self, root_node, serial):
        if root_node == None:
            # add nothing to the serial
            return # return void

        serial.append(root_node.value)
        
        if root_node.left == None and root_node.right == None:
            serial.append(0)
        elif root_node.left == None:
            serial.append("R")
        elif root_node.right == None:
            serial.append("L")
        else:
            serial.append(2)

        self.serialize_helper(root_node.left, serial)
        self.serialize_helper(root_node.right, serial)

    def serialize(self):
        serial = []
        self.serialize_helper(self.root, serial)

        return serial

    def deserialize(self, serial):
        if len(serial) == 0: # if the serial is empty
            return # return void
        
        node_value = serial.pop(0) # dequeues the list; "pops" the element at index 0
        node_children = serial.pop(0)

        new_root = BinaryNode(node_value)

        if node_children == 0:
            pass # do nothing
        elif node_children == "L":
            new_root.left = self.deserialize(serial)
        elif node_children == "R":
            new_root.right = self.deserialize(serial)
        elif node_children == 2:
            new_root.left = self.deserialize(serial)
            new_root.right = self.deserialize(serial)

        return new_root

    def deserialize_self(self, serial):
        # will rebuild the tree; all data from the previous tree will be lost
        self.root = self.deserialize(serial)

if __name__ == "__main__":
    test_tree = BinarySearchTree()
    
    test_arr = [23, 28, 16, 4, 25]
    for i in range(0, len(test_arr)):
        test_tree.insert(test_arr[i])

    print("test_tree.get_total_height() = ")
    print(test_tree.get_total_height())

    print("test_tree.get_weight_balance_factor() = ")
    print(test_tree.get_weight_balance_factor())

    print("test_tree.serialize() = ")
    print(test_tree.serialize())

    print("\nTesting deserialization ...")
    test_arr2 = [6, 2, 4, "R", 5, 0, 9, "L", 8, "L", 7, 0]
    test_tree.deserialize_self(test_arr2)
    print("test_tree.serialize() = ")
    print(test_tree.serialize())
    print("test_tree.get_weight_balance_factor() = ")
    print(test_tree.get_weight_balance_factor())
