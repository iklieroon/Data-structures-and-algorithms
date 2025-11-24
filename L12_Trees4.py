class Treenode:
    def __init__(self,x):
        self.data=x
        self.leftnode=None
        self.rightnode=None

def inordertraversal(root):
    if root is not None:
        inordertraversal(root.leftnode)
        print(root.data)
        inordertraversal(root.rightnode)

def insert(root,k):
    if root is None:
        return Treenode(k)
    if root.data>k:
        root.leftnode=insert(root.leftnode,k)
    else:
        root.rightnode=insert(root.rightnode,k)
    return root

def inordersucessor(root):
    current=root
    while current.leftnode is not None:
        current=current.leftnode
    return current

def delete(root,key):
    if root is None:
        return root
    if key<root.data:
        root.leftnode=delete(root.leftnode,key)
    elif key>root.data:
        root.rightnode=delete(root.rightnode,key)
    else:
        '''if root.leftnode is None:
            temp=root.rightnode
            root=None
            return temp
        elif root.rightnode is None:
            temp=root.leftnode
            root=None
            return temp'''
        if root.leftnode is None:
            return root.rightnode
        elif root.rightnode is None:
            return root.leftnode
        else:
            temp=inordersucessor(root.rightnode)
            print(temp.data)
            #t=root.data
            root.data=temp.data #replacing the current nodes data with the sucessors data
            #temp.data=t
            root.rightnode=delete(root.rightnode,temp.data)
    return root

n=int(input("how many nodes do you want in tree? "))
root=None
for i in range(n):
    x=int(input("enter each node value: "))
    root=insert(root,x)
inordertraversal(root)
root=delete(root,5)
inordertraversal(root)