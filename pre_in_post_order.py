class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data
 
# A function to do postorder tree traversal
def Postorder(root):
    if root:
        # First recur on left child
        Postorder(root.left)
 
        # the recur on right child
        Postorder(root.right)
 
        # now print the data of node
        print(root.val),
 
def Preorder(root):
    if root:
        print(root.val),
        Preorder(root.left)
        Preorder(root.right)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val),
        Inorder(root.right)

# Driver code
if __name__ == "__main__":
  root = Node(2)
  root.left = Node(4)
  root.right = Node(1)
  root.left.left = Node(7)
  root.right.right = Node(3)
  root.right.left = Node(8)
 
  # Function call
  print("\nPostorder traversal of binary tree :")
  Postorder(root)

  print("preorder :")
  Preorder(root)

  print("Inorder :")
  Inorder(root)
