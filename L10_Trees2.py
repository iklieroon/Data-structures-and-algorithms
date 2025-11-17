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

def search(root,key):
    if key==root.data:
        return root
    elif root.data>key and root.leftnode is not None:
        return search(root.leftchild,key)
    elif root.data<key and root.rightnode is not None:
        return search(root.rightchild,key)
    else:
        return -1

v=int(input("how many elements do you want in tree"))
root=None
for i in range(v):
    x=int(input("what element do you want in the node"))
    root=insert(root,x)

inordertraversal(root)

key=int(input("enter key that is to be searched"))
keynode=search(root,key)
if keynode==-1:
    print("key does not exist in the tree")
else:
    print("key exist",keynode.data)
