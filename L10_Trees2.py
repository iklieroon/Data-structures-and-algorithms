class Treenode:
    def __init__(self,x):
        self.data=x
        self.leftnode=None
        self.rightnode=None
def inordertraversal(root):
    if root is not None:
        if root.leftnode is not None:
            inordertraversal(root.leftnode)
        print(root.data)
        if root.rightnode is not None:
            inordertraversal(root.rightnode)

def insert(root,k):
    if root==None:
        return Treenode(k)
    if root.data>k:
        root.leftnode=insert(root.leftnode,k)
    else:
        root.rightnode=insert(root.rightnode,k)
    return root
