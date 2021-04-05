import sys

sys.stdin = open('input.txt')
words = input()
# words ='(()[[]])([])'

stack = []


def counting(words):
    """
    여는 태그 > stack에 넣기
    닫는 태그 ) ]일때 숫자가 여러개가 나올 수 있다.
    """
    for i in words:

        # print(stack)
        if i == ')':
            temp = 0
            # 숫자가 쌓여 있을 수도 있다!
            # 닫는태그와 여는 태그가 맞을때까지 반복
            while True:
                # 하나빼서
                now = stack.pop()
                # 올바른 닫는 태그
                if now == "(":
                    # 숫자없이 ()이 바로 들어왔으면 2 append
                    if temp == 0:
                        stack.append(2)
                        break
                    # (2) 일 경우 temp에 모두 저장되어있으므로 곱해준걸 append
                    else:
                        stack.append(2 * temp)
                        break
                # 옳지 않는 태그면 error처리
                elif now == "[":
                    result = 0
                    return result
                # 스택엔 숫자와 여는 태그뿐이므로
                # 숫자가 들어올때 처리
                else:
                    # 처음 pop 하자말자 숫자가 들어오면 temp에 저장
                    if temp == 0:
                        temp = now
                    # 숫자가 여러개가 들어오면 더해준다. ( 2 9 ) > 2*(2+9) 을 해주기 위해
                    else:
                        temp += now

        # ] 태그일때
        elif i == ']':
            temp = 0
            while True:
                now = stack.pop()
                # print(now)
                if now == "[":
                    if temp == 0:
                        # print(temp)
                        stack.append(3)
                        break
                    else:
                        stack.append(3 * temp)

                        break
                elif now == "(":
                    result = 0
                    return result
                else:
                    if temp == 0:
                        temp = now
                    else:
                        temp += now
        # 여는 태그일때
        else:
            stack.append(i)

    result = 0
    # 스택에 남은 숫자들 처리
    for i in stack:
        # 태그짝이 안맞으면 error 처리
        if i == '(' or i == '[':
            result = 0
            return result
        # 맞으면 더해서 반환
        else:
            result += i
    return result


print(counting(words))
