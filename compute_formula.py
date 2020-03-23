from logical_operators import neg_op, or_op, and_op, imp_op, eqv_op
from convert_formula import convert_to_rpn


def compute_boolean(f, c):
    f = f.split()
    n = len(f)
    for i in range(n):
        if f[i].isdigit():
            f[i] = c[int(f[i])]
    stack = []
    for term in f:
        if term.isdigit():
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


form_1 = 'p&(~p|U~p||)'
f = convert_to_rpn(form_1)
print(f)
for c in [('0', '0', '0'), ('0', '0', '1'), ('0', '1', '0'), ('1', '0', '0'), ('1', '1', '0'), ('1', '0', '1'),
          ('0', '1', '1'), ('1', '1', '1')]:
    print(compute_boolean(f, c))

