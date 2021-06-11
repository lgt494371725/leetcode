class Solution(object):
    def isSubtree(self, s, t):
        def traverse(root):
            stack=[root]
            list1=[]
            while stack:
                current=stack.pop()
                if current==None:
                    list1.append('x')
                else:
                    list1.append(current.val)
                if current:
                    stack.append(current.left)
                    stack.append(current.right)
            return list1
        s1=traverse(s)
        t1=traverse(t)
        s1=''.join(map(str,s1))
        t1=''.join(map(str,t1))
#字符串方法是有问题的，如果根的val是两位数的情况，就会错误的匹配
#可以通过改善方法来使这个方法成立
        return s1.find(t1)!=-1

class Solution(object):
    def isSubtree(self, s, t):
        def traverse(root):
            stack=[root]
            list1=[]
            while stack:
                current=stack.pop()
                if current==None:
                    list1.append('x')
                else:
                    list1.append(current.val)
                if current:
                    stack.append(current.left)
                    stack.append(current.right)
            return list1
        s1=traverse(s)
        t1=traverse(t)
        try:
            start=s1.index(t1[0])
            return s1[start:start+len(t1)]==t1
        except ValueError:
            return False
#这种也不行，因为index会找到最前面的数字，有相同数字的树出现的情况就不适用了

#正确方法，使用的是内置方法，或使用KMP方法去判断是否是子串
class Solution(object):
    def isSubtree(self, s, t):
        def traverse(root):
            stack=[root]
            list1=[]
            while stack:
                current=stack.pop()
                if current==None:
                    list1.append('x')
                else:
                    list1.append('|'+str(current.val)+'|')
                if current:
                    stack.append(current.left)
                    stack.append(current.right)
            return list1
        s1=traverse(s)
        t1=traverse(t)
        s1=''.join(s1)
        t1=''.join(t1)
        return s1.find(t1)!=-1
