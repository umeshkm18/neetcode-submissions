# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        lst = []
        if root:
            q.append(root)
        

        
        while len(q)>0:
            length = len(q)
            
            for i in range(length):
                curr = q.popleft()
                if i == length-1:        
                    
                    lst.append(curr.val)
                if curr.left:
                    q.append((curr.left))
                if curr.right:
                    q.append((curr.right))
     
        
        return lst


