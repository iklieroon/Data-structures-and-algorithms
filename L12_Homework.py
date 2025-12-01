class Treenode:
    def __init__(self,x):
        self.data=x
        self.leftnode=None
        self.rightnode=None

def preordertraversal(root):
    print(root.data)
    if root.leftnode!=None:
        preorder(root.leftnode)
    if root.rightnode!=None:
        preorder(root.rightnode)

def postordertraversal(root):
    if root.leftnode!=None:
        postorder(root.leftnode)
    if root.rightnode!=None:
        postorder(root.rightnode)
    print(root.data)

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
        return search(root.rightnode,key)
    else:
        return -1

n=int(input("how many nodes do you want in tree? "))
root=None
for i in range(n):
    x=int(input("enter each node value: "))
    root=insert(root,x)
v=input("choose 1 option: 1=insert, 2=search, 3=delete, 4=inorder traversal, 5=preorder traversal, 6=postorder traversal")

if v=="1":
    v2=int(input("what number do you want to insert: "))
    insert(root,v2)
elif v=="2":
    key=int(input("enter key that is to be searched"))
    keynode=search(root,key)
    if keynode==-1:
        print("key does not exist in the tree")
    else:
        print("key exist",keynode.data)
elif v=="3":
    root=delete(root,5)
    inordertraversal(root)
elif v=="4":
    inordertraversal(root)
elif v=="5":
    preordertraversal(root)
elif v=="6":
    postordertraversal(root)