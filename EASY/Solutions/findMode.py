class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if root == None:
                return
            
            count[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        count = defaultdict(int)
        dfs(root)

        maximum = max(count.values())
        return [key for key in count if count[key] == maximum]
