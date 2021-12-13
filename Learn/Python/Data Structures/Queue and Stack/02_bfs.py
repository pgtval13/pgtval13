from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getLonelyNodes(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []
        while len(queue):
            node = queue.popleft()
            if node.left:
                if not node.right:
                    res.append(node.left.val)
                queue.append(node.left)
            if node.right:
                if not node.left:
                    res.append(node.right.val)
                queue.append(node.right)
        return res

def averageOfLevels(self, root):
    queue = deque([root])   
    average_of_level = []
    
    while queue:
        
        # valid nodes on current level
        size = len(queue)        
        totalSum = 0
        
        for _ in range(size):
            
            # pop one node from traversal queue
            node = queue.popleft()
            
            # accumulate sum of current level
            totalSum += node.val
            
            # add left child if it exists
            if node.left:
                queue.append(node.left)
                
            # add right child if it exists
            if node.right:
                queue.append(node.right)
        
        # add current level's average value to list
        average_of_level.append(totalSum/size)
    
    return average_of_level