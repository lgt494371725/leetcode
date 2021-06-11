class BinarySearchTree: 
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):#调用树节点的迭代器
        return self.root.__iter__()
    
    def put(self,key,val):#插入key构造BST，根据key来决定插入位置
        if self.root:#如果根节点不为空
            self._put(key,val,self.root)
        else:#key作为根节点
            self.root=treeNode(key,val)
        self.size=self.size+1
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
                if currentNode.hasleftchild():
                    self._put(key,val,currentNode.leftchild)
                else:
                    currentNode.leftchild=TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasrightchild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightchild=TreeNode(key,val,parent=currentNode)
    def __setitem__(self,k,v):#魔法方法，a=BinarySearchTree,a[x]='y'时触发
        self.put(k,v)
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftchild)
        else:
            return self._get(key,currentNode.rightchild)
    def __getitem__(self,key):#a=BinarySearchTree,a['key']时触发
        return self.get(key)
    def __contains__(self,key):# in的魔法方法
        if self._get(key,self.root):
            return True
        else:
            return False
    def delete(self,key):
        if self.size>1:
            nodeToRemove=self._getkey(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size-=1
            else:
                raise KeyError('Error,key not in here')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size-=1
        else:
            raise KeyError('Error,key not in here')
    def __delitem__(self,key):#实现del a['key']的魔法方法
        self.delete(key)
    def remove(self,currentNode):#删除分成三种情况，没有子节点，1个子节点和2个子节点
        if currentNode.isleaf():#判断他是父结点的左子还是右子，设置为None
            if currentNode==currentNode.parent.leftchild:
                currentNode.parent.leftchild=None
            else:
                currentNode.parent.rightchild=None
        elif currentNode.hasbothchildren():#如果有两个子节点,需要找后继点，即右节点中最左的.后继节点要么是叶节点，要么只有一个右节点（因为是最小的不会有左子节点）
            succ=currentNode.findSuccessor()
            succ.spliceOut()#摘除后继节点
            currentNode.key=succ.key
            currentNode.payload=succ.payload
        else: #如果只有1个子节点，直接将子节点上移即可
            if currentNode.hasleftchild():
                if currentNode.isleftchild():#本身是父节点的左子节点。并只有一个左子节点
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.leftchild=currentNode.leftchild
                elif currentNode.isrightchild():#本身是父节点的右子节点。并只有一个左子节点
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.rightchild=currentNode.leftchild
                else:#本身是根节点，并只有左子节点
                    currentNode.replaceNodeData(currentNode.leftchild.key,currentNode.leftchild.payload,\
                                                currentNode.leftchild.leftchild,currentNode.leftchild.rightchild)
            else:#与上面相反，只有右子节点的情况
                if currentNode.isleftchild():
                    currentNode.rightchild.parent=currentNode.parent
                    currentNode.parent.leftchild=currentNode.rightchild
                elif currentNode.isrightchild():
                    currentNode.rightchild.parent=currentNode.parent
                    currentNode.parent.rightchild=currentNode.rightchild
                else:
                    currentNode.replaceNodeData(currentNode.rightchild.key,\
                                                currentNoed.rightchild.payload,\
                                                currentNode.rightchild.leftchild,
                                                currentNode.rightchild.rightchild)

        
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right
        self.parent=parent
    def hasleftchild(self):
        return self.leftchild
    def hasrightchild(self):
        return self.rightchild
    def isleftchild(self):
        return self.parent and self.parent.left.child==self
    def isrightchild(self):
        return self.parent and self.parent.right.child==self
    def isroot(self):
        return not self.parent
    def isleaf(self):
        return not(self.rightchild or self.leftchild)
    def hasanychildren(self):
        return self.rightchild or self.leftchild
    def hasbothchild(self):
        return self.rightchild and self.leftchild
    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftchild=lc
        self.rightchild=rc
        if self.hasleftchild():
            self.leftchild.parent=self
        if self.hasrightchild():
            self.rightchild.parent=self
    def __iter__(self):#中序遍历的迭代
        if self:
            if self.hasleftchild():
                for elem in self.leftchild:
                    yield elem
            yield slef.key
            if self.hasrightchild():
                for elem in self.rightchild
                    yield elem
    def findSuccessor(self):
        succ=None
        if self.hasrightchild():#找右子节点中最小的
            succ=self.rightchild.findMin()
        else:#不会碰到这段代码，因为寻找前提是拥有两个子节点然后来寻找后继
            if self.parent:
                if self.isleftchild():
                    succ=self.parent
                else:
                    self.parent.rightchild=None
                    succ=self.parent.findSuccessor()
                    self.parent.rightchild=self
        return succ
    def findMin(self):
        current=self
        while current.hasleftchild():#找到最左边的就是最小的
            current=current.leftchild
        return current
    def spliceOut(self):
        if self.isleaf():
            if self.isleftchild():
                self.parent.leftchild=None
            else:
                self.parent.rightchild=None
        elif:#如果不是叶节点，就只有右子节点，理由在上面
             if self.isleftchild():#即本身是左子节点并有右子节点，就直接把右子节点给父结点的左子节点
                 self.parent.leftchild=self.rightchild
             else:
                self.parent.rightchild=self.rightchild
            self.rightchild.parent=self.parent
            
        

            
