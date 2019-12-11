'''
Given a linked list rearrange the node values such that they appear in alternating 

low->high->low etc.


'''

def alternate(node):
    prev = node
    curr = node.next

    while curr:
        if prev.val > curr.val:
            prev.val, curr.val = curr.val, prev.val
        
        if not curr.next:
            break

        if curr.next.data > curr.data