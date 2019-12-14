'''
Compute the maximum of k-length subarrays
'''


#naive approach 

def max_of_subArray(lst, k):
    for i in range(len(lst)-k+1):
        print(max(lst[i:i+k]))


from collections import deque
def maxOfSubarray(lst, k):
    q = deque()
    for i in range(k):
        print(q)
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(q)


print(maxOfSubarray([10,5,2,7,8,7],3))
