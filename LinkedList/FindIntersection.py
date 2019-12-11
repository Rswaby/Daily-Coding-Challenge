'''
Given two singly linked list that intersect at some point find 
the interecting no
de assume the list are non-cyclical. 

A = 3 -> 7 -\ 
             8 -> 10
B = 99 - 1 -/

return 8
'''


def llLength(head):
    if head == None:
        return 0
    return 1 + llLength(head.next)


def intersect(AList, BList):
    lenA,lenB = llLength(AList), llLength(BList)
    currA,currB = AList, BList


    if lenA > lenB:
        for _ in range(lenA-lenB):
            currA = currA.next
    else:
        for _ in range(lenB-lenA):
            currB = currB.next
    

    while(currA!=currB):
        currA = currA.next
        currB = currB.next
    
    return currA