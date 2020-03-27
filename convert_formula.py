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
    f = re.sub('N', ' N ', f)
    return f


def space_out(f):
    f = re.sub(r'\(', '( ', f)
    f = re.sub(r'\)', ') ', f)
    f = re.sub(r']', ' ] ', f)
    return f


def match_parenthesis(s, i):
    stack = []
    for index in range(i, len(s)):
        if s[index] == '(':
            stack.append('(')
        elif s[index] == ')':
            stack.pop()
        if not stack:
            return index


def match_number_end(s, i):
    index = i
    while s[index].isdigit():
        index += 1
    return index


def add_neg_brackets(f):
    pattern = '[~]+'
    while '~' in f:
        match = re.search(pattern, f)
        index = match.end()
        length = match.end() - match.start()
        if index < len(f) and f[index] == '(':
            end = match_parenthesis(f, index)
            seq = list(f)
            for _ in range(length):
                seq.insert(end+1, ']')
                seq[seq.index('~')] = 'N'
            f = ''.join(seq)
        elif index < len(f) and f[index].isdigit():
            end = match_number_end(f, index)
            seq = list(f)
            for _ in range(length):
                seq.insert(end, ']')
                seq[seq.index('~')] = 'N'
            f = ''.join(seq)
        else:
            raise IndexError
    return f


def render_raw_formula(f):
    f = convert_variables(f)
    if '|' in f:
        return None
    f = add_neg_brackets(f)
    f = convert_operators(f)
    f = space_out(f)
    cl_num = f.count(')')
    op_num = f.count('C') + f.count('A') + f.count('K') + f.count('E')
    if cl_num < op_num:
        f = f'( {f} )'
    return f


def check_parenthesis(f):
    f = render_raw_formula(f)
    if f is None:
        return False
    stack = []
    try:
        for term in f:
            if term == '(':
                stack.append(term)
            if term == ')':
                stack.pop()
    except ValueError:
        return False
    if stack:
        return False
    return True


def convert_to_rpn(f):
    if not check_parenthesis(f):
        raise IndexError
    f = render_raw_formula(f)
    if f == '( 0 )':
        return '0'
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

