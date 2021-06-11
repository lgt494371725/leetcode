class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        else:return min(self.minDepth(root.left),self.minDepth(root.right))+1
#广度
class Solution:
    def minDepth(self, root) :
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0
