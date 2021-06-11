#dfs(递归)
class Solution(object):
    def binaryTreePaths(self, root):
        list1=[]
        s=''
        def traverse(root,s):
            if not root:
                return 
            if not root.left and not root.right:
                s=s+'{}'.format(root.val)
                list1.append(s)
            else:
                s+='{}->'.format(root.val)
                if root.left:
                    traverse(root.left,s)
                if root.right:
                    traverse(root.right,s) 
        traverse(root,s)
        return list1
#队列
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = list()
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))
                
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths
#第三种，与队列法相似，用栈实现非递归dfs
class Solution:
    def binaryTreePaths(self, root):
        paths = list()
        if not root:
            return paths

        node_stack = [root]
        path_stack = [str(root.val)]

        while node_stack:
            node = node_stack.pop()
            path = path_stack.pop()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_stack.append(node.left)
                    path_stack.append(path + '->' + str(node.left.val))
                
                if node.right:
                    node_stack.append(node.right)
                    path_stack.append(path + '->' + str(node.right.val))
        return paths
