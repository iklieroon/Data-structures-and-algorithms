class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
def preorder(root):
    print(root.data)
    if root.leftnode!=None:
        preorder(root.leftnode)
    if root.rightnode!=None:
        preorder(root.rightnode)
def postorder(root):
    if root.leftnode!=None:
        postorder(root.leftnode)
    if root.rightnode!=None:
        postorder(root.rightnode)
    print(root.data)
def inorder(root):
    if root.leftnode!=None:
        inorder(root.leftnode)
    print(root.data)
    if root.rightnode!=None:
        inorder(root.rightnode)

root=Treenode(5)
root.leftnode=Treenode(4)
root.leftnode.leftnode=Treenode(2)
root.rightnode=Treenode(8)
root.rightnode.leftnode=Treenode(7)
root.rightnode.rightnode=Treenode(9)

i=input("choose an option: option 1=preorder option 2=postorder option 3=inorder")
if i==1:
    preorder(root)
elif i==2:
    postorder(root)
elif i==3:
    inorder(root)
