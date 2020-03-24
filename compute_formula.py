from logical_operators import neg_op, or_op, and_op, imp_op, eqv_op
from convert_formula import convert_to_rpn, var_number


def compute_boolean(f, c):
    f = f.split()
    n = len(f)
    for i in range(n):
        if f[i].isdigit():
            f[i] = c[int(f[i])]
    stack = []
    for term in f:
        if type(term) == int:
            stack.append(term)
        if term == 'N':
            val = stack.pop()
            stack.append(neg_op(val))
        if term == 'A':
            val_1 = stack.pop()
            val_2 = stack.pop()
            stack.append(or_op(val_1, val_2))
        if term == 'K':
            val_1 = stack.pop()
            val_2 = stack.pop()
            stack.append(and_op(val_1, val_2))
        if term == 'C':
            val_1 = stack.pop()
            val_2 = stack.pop()
            stack.append(imp_op(val_2, val_1))
        if term == 'E':
            val_1 = stack.pop()
            val_2 = stack.pop()
            stack.append(eqv_op(val_1, val_2))
    return stack.pop()


def pow_2(n):
    i = 0
    while n % 2 == 0:
        n //= 2
        i += 1
    return i


def search_for_counterexample(form):
    f = convert_to_rpn(form)
    n = var_number(form)
    c = [0] * n
    p = 0
    k = 0
    while p < n:
        if compute_boolean(f, c) == 0:
            return c
        k += 1
        p = pow_2(k)
        if p < n:
            c[p] = 1 - c[p]
    return None


def get_answer(form):
    answer = search_for_counterexample(form)
    if answer is None:
        return 'TAUTOLOGY'
    else:
        answer = [str(b) for b in answer]
        return 'Invalid for: ' + ''.join(answer)




