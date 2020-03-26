import re


def convert_variables(f):
    pattern = r'p\|*'
    var = re.findall(pattern, f)
    var = list(set(var))
    var.sort(key=lambda x: len(x))
    var.reverse()
    num = len(var) - 1
    for match in var:
        match = re.escape(match)
        f = re.sub(match, f'{num} ', f)
        num -= 1
    return f


def var_number(f):
    pattern = r'p\|*'
    var = re.findall(pattern, f)
    var = list(set(var))
    return len(var)


def convert_operators(f):
    f = re.sub('<=>', 'E ', f)
    f = re.sub('=>', 'C ', f)
    f = re.sub('U', 'A ', f)
    f = re.sub('&', 'K ', f)
    f = re.sub('~', '~  ', f)
    return f


def space_out(f):
    f = re.sub(r'\(', '( ', f)
    f = re.sub(r'\)', ') ', f)
    return f


def match_closing_parenthesis(s, i):
    stack = []
    for index in range(i, len(s)):
        if s[index] == '(':
            stack.append('(')
        elif s[index] == ')':
            stack.pop()
        if not stack:
            return index


def fill_closing_brackets(f):
    f = f.split()
    while '~' in f:
        start = f.index('~')
        if f[start+1].isdigit():
            f.insert(start+2, ']')
            f[f.index('~')] = 'N'
        else:
            end = match_closing_parenthesis(f, start+1)
            f.insert(end+1, ']')
            f[f.index('~')] = 'N'
    return ' '.join(f)


def render_raw_formula(f):
    f = convert_variables(f)
    if '|' in f:
        return None
    f = convert_operators(f)
    f = space_out(f)
    f = fill_closing_brackets(f)
    if f[-1] != ']':
        f = f'( {f} )'
    return f


def convert_to_rpn(f):
    f = render_raw_formula(f)
    stack = []
    for term in f:
        if term == ']':
            f_1 = stack.pop()
            new_top = f'{f_1} {stack.pop()}'
            stack.append(new_top)
        if term == ')':
            f_1 = stack.pop()
            op = stack.pop()
            f_2 = stack.pop()
            new_top = f'{f_2} {f_1} {op}'
            stack.append(new_top)
        if term.isalnum():
            stack.append(term)
    rpn = stack.pop()
    if stack:
        raise IndexError
    return rpn

