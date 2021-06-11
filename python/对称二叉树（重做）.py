class Solution(object):
    def isSymmetric(self, root):
        def check(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val!=node2.val:
                return False
            else:
                return check(node1.left,node2.right) and check(node1.right,node2.left)
        return check(root,root)#若root为空，这样的写法不会出错
class Solution(object):
    def isSymmetric(self, root):
        queue=[root]
        while queue:
            next_queue=[]#每回循环都要重置这两个条件
            layer=[]#储存数值
            for node in queue:
                if not node:
                    layer.append(node)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                layer.append(node.val)
            if layer!=layer[::-1]:
                return False
            queue=next_queue
        return True
