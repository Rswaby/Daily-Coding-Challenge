def reversePolishNotation(arr):
  solution = []

  for operands in arr:
    print('operands: ', operands)
    if operands not in ['+','-','*','/']:
      solution.append(int(operands))
    
    else:
      operand1, operand2 = solution.pop(), solution.pop()
      print("op1",operand1)
      print("op2",operand2)
      if operands == '+':
        solution.append(operand2 + operand1)
        print('op2+op1',operand2+operand1)
      elif operands == '-':
        solution.append(operand2 - operand1)
        print('op2-op1',operand2-operand1)
      elif operands == '*':
        solution.append(operand2 * operand1)
        print('op2*op1',operand2*operand1)
      elif operands == '/':
        solution.append(int(operand2 / operand1))
        print('op2/op1=',operand2 / operand1)
  
  return solution.pop()

test1 = ["4", "13", "5", "/", "+"]

print(reversePolishNotation(test1))
