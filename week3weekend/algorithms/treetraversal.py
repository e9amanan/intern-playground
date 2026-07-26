from typing import Optional
from collections import deque

class Node:
    def __init__(self,val:int=0, left: Optional['Node']=None,right:Optional['Node']=None):
        self.val=val
        self.left=left
        self.right=right

def bfs_level_order(root:Optional[Node])-> list[list[int]]:
    if not root:
        return[]
    
    result=[]
    queue=deque([root])

    while queue:
        level_size=len(queue)
        current_level=[]

        for _ in range(level_size):
            node=queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
    
    return result

def dfs_iterative(root:Optional[Node])->list[int]:

    if not root:
        return[]
    
    result=[]
    stack=[root]

    while stack:
        node=stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left: 
            stack.append(node.left)

    return result

