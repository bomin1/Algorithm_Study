def cal(my_str,stack, equation):
    for i in my_str:
        if i == '(':
            stack.append(i)
            equation.append("+2(")
        elif i == '[':
            stack.append(i)
            equation.append('+3(')
        elif i == ')':
            if stack and stack[-1]=='(':
                stack.pop()
                equation.append(')')
            else:
                return
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                equation.append(')')
            else:
                return -1
        else:
            return -1
    if not stack:
        return 0
    else:
        return -1


my_str = '(()[[]])([])'
print(my_str)
stack = []
equation = []
res = cal(my_str,stack, equation)
# print(equation)
# ['+2(', '+2(', ')', '+3(', '+3(']

equation="".join(equation)
print(equation)
# +2(+2()+3(+3(


if res ==-1:
    print(0)
else:
    equation=equation.replace("()","")
    print('------------')
    print(equation)
    print('+2*(2+3*(3))+2*(+3)')
    print('------------------')

    equation = equation.replace("(+", "*(")
    print(equation)

    print(eval(equation))

