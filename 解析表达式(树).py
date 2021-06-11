import  operator
from Stack import *
from BinaryTree import *
def buildParseTree(fpexp):#构造解析树
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree("")
    pStack.push(eTree)
    currentTree=eTree#当前节点
    for i in fplist:
        if i=="(":
            currentTree.insertleft('')
            pStack.push(currentTree)
            currentTree=currentTree.getleftchild()
        elif i not in "+-*/)":
            currentTree.setrootval(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in "+-*/":
            currentTree.setrootval(i)
            currentTree.insertright('')
            pStack.push(currentTree)
            currentTree=currentTree.getrightchild()
        elif i ==")":
            currentTree=pStack.pop()
        else:
            raise ValueError
    return eTree
def evaluate(parseTree):#表达式求值
    opers={'+':operator.add,'-':operator.sub,\
           '*':operator.mul,'/':operator.truediv}
    leftC=parseTree.getleftchild()
    rightC=parseTree.getrightchild()
    if leftC and rightC:
        fn=opers[parseTree.getrootval()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getrootval()
