class MinStack(object):

    def __init__(self):
        self.stack=list()
        self.minpos=-1
  


    def push(self, x):
        if self.stack==[]:
            self.minpos=0
        else:
            self.minpos=self.minpos if x>self.stack[self.minpos] else len(self.stack)
        #注意，在插入之前判断的长度
        self.stack.append(x)
    
    


    def pop(self):
        if self.minpos==len(self.stack)-1:#注意这里要减一
            self.stack.pop()
            self.minpos=self.stack.index(min(self.stack)) if self.stack else -1
            #要考虑到弹出后变成空栈的情况，不能对空列表用Min函数
        else: self.stack.pop()


    def top(self):
        return self.stack[-1]
