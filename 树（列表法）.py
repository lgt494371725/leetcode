def BinaryTree(r):
    return [r,[],[]]
def insertLeft(root,newBranch):
    t=root.pop(1)#把原先根的左子树pop出来
    if len(t)>1:#如果大于1说明原先有左子树
        root.insert(1,[newBranch,t,[]])#插入新的左子树，然后把原先的左子树作为新左子树的左子树
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
def getRootval(root):
    return root[0]#取得根节点数据
def setRootval(root,newVal):
    root[0]=newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]
