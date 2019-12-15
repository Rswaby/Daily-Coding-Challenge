def count_univals(root):

    def _unival(root):

        if root is None:
            return 0, True
        
        leftCount,leftValid = _unival(root.left)
        rightCount,rightValid = _unival(root.left)

        total = leftCount + rightCount

        if leftValid and rightValid:
            if root.left != None and root.value != root.left.value:
                return total, False
            if root.right != None and root.right != root.right.value:
                return total, False
            return 1 + total, True
        return total, False