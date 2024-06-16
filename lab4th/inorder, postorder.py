class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    if inorder:
        root_data = postorder.pop(-1)
        root = Node(root_data)
        root_index = inorder.index(root_data)
        root.right = build_tree(inorder[root_index+1:], postorder)
        root.left = build_tree(inorder[:root_index], postorder)
        return root
    return None

def print_tree(node, depth=0, node_type='root'):
    if node is not None:
        print('    '*depth + '(' + node_type + ', ' + node.data + ')')
        print_tree(node.left, depth+1, 'left')
        print_tree(node.right, depth+1, 'right')

inorder_list = ['d', 'b', 'h', 'e', 'i','a', 'f', 'c', 'g']
postorder_list = ['d', 'h', 'i', 'e', 'b', 'f', 'g', 'c','a']

try:
    tree = build_tree(inorder_list, postorder_list)
    print_tree(tree)
except ValueError:
    print("error: Tree cannot be constructed using these two traversals")
