"""
File: arithExp.py
Author: Man-Chi Leung
A program for evaluating arithmetic expressions.
"""

from liststack import ListStack


def infix_to_postfix(infix_exp):
    """ Converts infix expression to postfix expression.
    Return postfix expression.
    Operands/operators are separated by spaces in expressions."""
    result = ""
    stack = ListStack(infix_exp)
    operators = "+-*/^"
    order = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Finding operand
    for i in infix_exp:
        if i not in operators:
            result += i

        # Finding left parenthesis:
        elif i == '(':
            stack.push(i)

        # Finding right parentheses:
        elif i == ')':
            while stack and stack.peek() != '(':
                result += stack.pop()
            stack.pop()

        else:
            while stack.peek() != '(' and order[i] <= order[stack.peek()]:
                result += stack.pop()
            stack.push(i)
    while stack:
        result += stack.pop()

    return result


def main():
    infix = "4 + 5 * 6 - 3"
    postfix = infix_to_postfix(infix)
    print("Infix expression:", infix)
    print("postfix expression:", postfix)
    print()

    infix = "( 4 + 5 ) * ( 6 - 3 )"
    postfix = infix_to_postfix(infix)
    print("Infix expression:", infix)
    print("postfix expression:", postfix)


if __name__ == "__main__":
    main()
