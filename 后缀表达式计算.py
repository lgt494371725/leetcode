from Stack import *
def postfixEval(postfix):
    operandStack=Stack()
    tokenlist=postfix.split()
    for token in tokenlist:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operandr=operandStack.pop()
            operandl=operandStack.pop()
            result=doMath(token,operandl,operandr)
            operandStack.push(result)
    return operandStack.pop()
def doMath(op,op1,op2):
    if op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op1+op2
    else:
        return op1-op2
