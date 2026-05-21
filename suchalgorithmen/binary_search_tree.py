class Node():
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None 

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

def search(root, target): 
    if root is None:
        return False 
    
    if target == root.value:
        return True 
    elif target < root.value:
        return search(root.left, target)
    else: 
        return search(root.right, target)
    
def inorder_traversial(root):
    if root is None:
        return [] 
    
    return inorder_traversial(root.left) + [root.value] + inorder_traversial(root.right)

bst = Node(3)
bst = insert(bst, 5)

ins = [0,5,7,3,4,8,2,1]
for num in ins:
    bst = insert(bst, num)


print(inorder_traversial(bst))