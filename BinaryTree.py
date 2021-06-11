class BinaryTree:
    def __init__(self,attr):
        self.key=attr
        self.leftchild=None
        self.rightchild=None
    def insertleft(self,newattr):
        if self.leftchild==None:  
            self.leftchild=BinaryTree(newattr)
        else:
            t=BinaryTree(newattr)
            t.leftchild=self.leftchild
            self.leftchild=t
    def insertright(self,newattr):
        if self.rightchild==None:  
            self.rightchild=BinaryTree(newattr)
        else:
            t=BinaryTree(newattr)
            t.rightchild=self.rightchild
            self.rightchild=t
    def getrightchild(self):
        return self.rightchild
    def getleftchild(self):
        return self.leftchild
    def setrootval(self,obj):
        self.key=obj
    def getrootval(self):
        return self.key
