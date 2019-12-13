"""
Given a string of round curly and square opening ang closing brackets 
return wether the barckes are balanced(well-formed)
"""

def balanced(braces):
    stack = []
    for brace in braces:
        if brace in ["(","[","{"]:
            stack.append(brace)
        else:
            if not stack:
                return False
            
            if (brace == ")") and stack[-1] != "(" or \
                (brace == "}") and stack[-1] != "{" or \
                    (brace == "]") and stack[-1] != "[":
                return False
            stack.pop
    return True
