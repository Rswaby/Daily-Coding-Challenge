"""
Simple Queue Example

"""

#from queue import deque
from collections import deque

queue = deque()
queue.append(4)
queue.append(5)
queue.appendleft(6)

#queue looks like this [6,4,5]