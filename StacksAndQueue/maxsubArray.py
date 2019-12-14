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
        #print(q)
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    #print(q)

    #loop invariant: q is a list of indecies where
    #there corresponding values are in desending order

    for i in range(k, len(lst)):
        print(q[0])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(q[0])

print(maxOfSubarray([2,5,2,7,8,7],3))
