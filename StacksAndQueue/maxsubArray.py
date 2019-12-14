'''
Compute the maximum of k-length subarrays
'''


#naive approach 

def max_of_subArray(lst, k):
    for i in range(len(lst)-k+1):
        print(max(lst[i:i+k]))