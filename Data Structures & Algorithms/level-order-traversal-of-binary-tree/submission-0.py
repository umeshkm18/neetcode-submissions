# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
I will use the BFS and go layer by layer
in first layer I will append my root into the queue and then I will have it appended to my list. I will have outer list where my inner list will be appended.
I will add the left and righ child from the root and I will also append my 


"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        newlst = []

        if root:
            q.append(root)
        


        while len(q)>0:
            lst = []
            for val in range(len(q)):
                curr = q.popleft()
                lst.append((curr.val))

                if curr.left:
                    q.append((curr.left))
                if curr.right:
                    q.append((curr.right))
            newlst.append(lst)
            # lst.clear()

        
        return newlst