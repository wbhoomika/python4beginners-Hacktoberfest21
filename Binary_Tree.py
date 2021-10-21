class TreeNode():
    #Constructor function
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    #Maximun Height of the Binary Tree
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    #Size of the Tree
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    #Inorder Traversal
    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    #Preorder Traversal
    def preorderTraversal(self):
        if root is None:
            return []
        return([self.val]+TreeNode.postorderTraversal(self.left)+
               TreeNode.postorderTraversal(self.right))
    #Postorder Traversal
    def postorderTraversal(self):
        if root is None:
            return []
        return(TreeNode.postorderTraversal(self.left)+
               TreeNode.postorderTraversal(self.right)+[self.val])
    #Returns the Nodes of the Tree in a Tuple
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    #Taking input as a tuple and converting it in a Binary Tree
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node