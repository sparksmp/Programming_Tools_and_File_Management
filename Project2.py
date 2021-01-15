
class TernaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.middle = None
    
    def insert_node(self, new_value):
        if new_value < self.value:
            if self.left == None:
                self.left = TernaryTree(new_value)
            else:
                self.left.insert_node(new_value)
        elif new_value > self.value:
            if self.right == None:
                self.right = TernaryTree(new_value)
            else:
                self.right.insert_node(new_value)
        else:
            if self.middle == None:
                self.middle = TernaryTree(new_value)
            else:
                self.middle.insert_node(new_value)
    
    def generate_tree(self, L):
        self.value = L[0]
        for element in L[1:]:
            self.insert_node(element)
    
    def traverse_WLMR(self):
        #Write, go left, go middle, go right.
        print(self.value)
        if self.left != None:
            self.left.traverse_WLMR()
        if self.middle != None:
            self.middle.traverse_WLMR()
        if self.right != None:
            self.right.traverse_WLMR()

    def non_leaf_count(self, node = []):
        if self.left != None or self.right != None or self.middle != None:
            node.append(self.value)
        if self.left != None:
            self.left.non_leaf_count()
        if self.middle != None:
            self.middle.non_leaf_count()
        if self.right != None:
            self.right.non_leaf_count()
        return len(node)
        
    def leaf_count(self, leaf = []):
        if self.left == None and self.right == None and self.middle == None:
            leaf.append(self.value)
        else:
            if self.left != None:
                self.left.leaf_count()
            if self.middle != None:
                self.middle.leaf_count()
            if self.right != None:
                self.right.leaf_count()
        return len(leaf)

    def degree_two_nodes_count(self, deg_2 = []):
        # returns the number of nodes that have exactly TWO edges coming out of them
        if self.left != None and self.right != None and self.middle == None:
            deg_2.append(self.value)
        if self.left != None and self.right == None and self.middle != None:
            deg_2.append(self.value)
        if self.left == None and self.right != None and self.middle != None:
            deg_2.append(self.value)
        if self.left != None and self.right != None and self.middle != None:
            self.right.degree_two_nodes_count()
        if self.left != None and self.right != None and self.middle != None:
            self.left.degree_two_nodes_count()
        if self.left != None and self.right != None and self.middle != None:
            self.middle.degree_two_nodes_count()
        return len(deg_2)

    def tree_depth(self):
    # returns the depth of the tree. initial root node is depth 0
        return self.depth(self)

    def depth(self, root):
        if root is None:
            return 0
        if root.left == None and root.right == None and root.middle == None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        middle_depth = self.depth(root.middle)
        return max(left_depth, right_depth, middle_depth) + 1


def main():
    L = [4, 1, 2, 2, 3, 1, 0, 4, 6, 5, 6, 4]
    T = TernaryTree(L)
    T.generate_tree(L)
    print('Traverse WLMR:')
    T.traverse_WLMR()
    print('Non leaf count:')
    print(T.non_leaf_count())
    print("Leaf count:")
    print(T.leaf_count())
    print('Degree 2 nodes:')
    print(T.degree_two_nodes_count())
    print("Tree Depth:")
    print(T.tree_depth())

main()