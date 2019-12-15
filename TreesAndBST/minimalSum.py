'''
Given a binary tree return the level of the tree that has a minimum sum 
the leel of the node is defined as the number of connections required to get o the root

'''


import TreesAndBST.TreeNode
from collections import defaultdict, deque
def smallestLevel(root):
    que = deque([])
    que.append((root,0))

    level_sum = defaultdict(int)

    while que:
        node, level = que.popleft()

        if node.right:
            que.append((node.right, level+1))
        if node.left:
            que.append((node.left, level+1))
    return min(level_sum,key=level_sum.get)
