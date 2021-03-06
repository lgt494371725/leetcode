class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        elif root.children==[]:
            return 1
        else:
            height=[self.maxDepth(c) for c in root.children]
        return max(height)+1
class Solution(object):
    def maxDepth(self, root):

        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))
        return depth
