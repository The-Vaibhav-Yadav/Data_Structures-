class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if inorder:
        root_data = preorder.pop(0)
        root = Node(root_data)
        root_index = inorder.index(root_data)
        root.left = build_tree(preorder, inorder[:root_index])
        root.right = build_tree(preorder, inorder[root_index+1:])
        return root
    return None

def print_tree(node, depth=0, node_type='root'):
    if node is not None:
        print('    '*depth + '(' + node_type + ', ' + node.value + ')')
        print_tree(node.left, depth+1, 'left')
        print_tree(node.right, depth+1, 'right')

preorder_list = ['a', 'b', 'd', 'e', 'h', 'i', 'c', 'f', 'g']
inorder_list = ['d', 'b', 'h', 'e', 'i','a', 'f', 'c', 'g']

try:
    tree = build_tree(preorder_list, inorder_list)
    print_tree(tree)
except ValueError:
    print("error: Tree cannot be constructed using these two traversals")