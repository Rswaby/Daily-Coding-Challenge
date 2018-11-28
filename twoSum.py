'''
this problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
def twoSum(arr,k):
    loop_up = dict();

    for i in range(len(arr)):
        differnce = k-arr[i]
        #print(differnce)

        if not loop_up.get(differnce):
            loop_up[arr[i]] = differnce
        else:
            return True
    
    return False

arr = [4,3,2,1,8]
k = 3
print(twoSum(arr,k))
