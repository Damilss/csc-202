from __future__ import annotations

from array_stack import * 


def postfix_eval(input_string: str) -> float:
    """postfix evaluation from a string. Given tokens are properly spaced
    and everything is correct.
    """
    tokens = input_string.split()
    if len(tokens) == 0:
        raise ValueError("empty input")

    stack = empty_stack()
    operators = {"+", "-", "*", "/", "^"}

    for tok in tokens:
        try:
            num = float(tok)
            push(stack, num)
            continue
        except ValueError:
            pass

        if tok in operators:
            try:
                right = pop(stack)
                left = pop(stack)
            except IndexError:
                raise ValueError("not enough operands")

            if tok == "+":
                push(stack, left + right)
            elif tok == "-":
                push(stack, left - right)
            elif tok == "*":
                push(stack, left * right)
            elif tok == "/":
                push(stack, left / right)
            else:  # "^"
                push(stack, left ** right)
        else:
            raise ValueError("invalid token")

    if size(stack) < 1:
        raise ValueError("not enough operands")
    if size(stack) > 1:
        raise ValueError("too many operands")

    return pop(stack)


def infix_to_postfix(input_string: str) -> str:
    """Convert a space-separated infix expression to postfix (RPN).
    Given tokens are separated by exactly one space and the expression 
    is correct."""
    
    if input_string is None:
        raise ValueError("empty input")

    tokens = input_string.split()
    if len(tokens) == 0:
        raise ValueError("empty input")

    prec = {
        '^': 3,
        '*': 2, '/': 2, '//': 2,
        '+': 1, '-': 1,
    }
    
    right_assoc = {'^'}

    out_tokens: list[str] = []
    op_stack = empty_stack()

    def is_operator(t: str) -> bool:
        return t in prec

    def is_operand(t: str) -> bool:
        
        if t in ("(", ")"):
            return False
        if is_operator(t):
            return False
       
        try:
            float(t)
            return True
        except ValueError:
            return True

    for tok in tokens:
        if is_operand(tok):
            out_tokens.append(tok)
            continue

        if tok == '(':
            push(op_stack, tok)
            continue

        if tok == ')':
            
            while size(op_stack) > 0 and peek(op_stack) != '(':
                out_tokens.append(pop(op_stack))
            
            if size(op_stack) == 0:
            
                raise ValueError("mismatched parenthesis")
            pop(op_stack)  # discard '('
            continue

        
        if is_operator(tok):
            while size(op_stack) > 0 and is_operator(peek(op_stack)):
                top = peek(op_stack)
                top_prec = prec[top]
                cur_prec = prec[tok]

                if (top_prec > cur_prec) or (top_prec == cur_prec and tok not in right_assoc):
                    out_tokens.append(pop(op_stack))
                    continue
                break

            push(op_stack, tok)
            continue

        raise ValueError("invalid token")

    while size(op_stack) > 0:
        top = pop(op_stack)
        if top in ("(", ")"):
            raise ValueError("mismatched parenthesis")
        out_tokens.append(top)

    return " ".join(out_tokens) 
