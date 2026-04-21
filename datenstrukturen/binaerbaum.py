class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# --- Traversierungs-Funktionen ---

def preorder(node):
    """Wurzel -> Links -> Rechts"""
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    """Links -> Wurzel -> Rechts"""
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def postorder(node):
    """Links -> Rechts -> Wurzel"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

# --- Erweiterung: Grafische Ausgabe ---

def display_tree(node, level=0, prefix="Root: "):
    """Gibt die Baumstruktur mit Einrückungen aus."""
    if node is not None:
        print("    " * level + prefix + str(node.value))
        if node.left or node.right:
            display_tree(node.left, level + 1, "L─── ")
            display_tree(node.right, level + 1, "R─── ")

# --- Hauptprogramm ---

if __name__ == "__main__":
    # 1. Baum manuell aufbauen (Beispiel mit 6 Knoten)
    # Struktur:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # 2. Grafische Darstellung anzeigen
    print("Grafische Baumstruktur:")
    display_tree(root)
    print("-" * 30)

    # 3. Traversierungen testen
    print("Preorder Traversierung (W-L-R):")
    preorder(root)
    print("\n")

    print("Inorder Traversierung (L-W-R):")
    inorder(root)
    print("\n")

    print("Postorder Traversierung (L-R-W):")
    postorder(root)
    print("\n")