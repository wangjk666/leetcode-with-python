def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))              
            else:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    result = a // b
                    result = result + 1 if result<0 and a%b!=0 else result                
                stack.append(result)
        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))

                



                    

            