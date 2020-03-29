import re


def convert_variables(f):
    """the function substitutes any variable in the formula f for a natural number, thus created natural numbers are
    0, 1,..., k-1 where k is the number of distinct variables in the formula f"""
    pattern = r'p\|*'
    var = re.findall(pattern, f)
    var = list(set(var))
    var.sort(key=lambda x: len(x))
    var.reverse()
    num = len(var) - 1
    for match in var:
        match = re.escape(match)
        f = re.sub(match, f'{num}', f)
        num -= 1
    return f


def var_number(f):
    """the function returns the number of variables in the formula f"""
    pattern = r'p\|*'
    var = re.findall(pattern, f)
    var = list(set(var))
    return len(var)


def convert_operators(f):
    """the function substitutes logical connectives in f for their counterparts in the parenthesis-free notation"""
    f = re.sub('<=>', 'E ', f)
    f = re.sub('=>', 'C ', f)
    f = re.sub('U', 'A ', f)
    f = re.sub('&', 'K ', f)
    f = re.sub('N', 'N ', f)
    return f


def add_space(f):
    """this is a technical function that adds spaces between signs so as to separate
    units of different roles"""
    f = re.sub(r'\(', '( ', f)
    f = re.sub(r'\)', ') ', f)
    f = re.sub(r']', '] ', f)
    borders = re.findall(r'\d[^\d]', f)
    for b in borders:
        rb = re.escape(b)
        f = re.sub(rb, f'{b[0]} {b[1]}', f)
    return f


def match_parenthesis(s, i):
    """this is a technical function that finds the index in the string s of the closing parenthesis corresponding to
    the opening one at the index i"""
    stack = []
    for index in range(i, len(s)):
        if s[index] == '(':
            stack.append('(')
        elif s[index] == ')':
            stack.pop()
        if not stack:
            return index


def match_number_end(s, i):
    """the function finds the first index after i for which s[index] is not a digit"""
    index = i
    while index < len(s) and s[index].isdigit():
        index += 1
    return index


def add_neg_brackets(f):
    """the function adds sign ']' after any negation phrase (negated subformula) that lies in f - by convention we
    assume that formula f (given by the user) does not contain parenthesis for negations so for further processing
    those brackets need to be automatically added"""
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
    """the function finally renders a raw formula given by the user into a form suitable for later processing"""
    f = convert_variables(f)
    if '|' in f:
        return None
    f = add_neg_brackets(f)
    f = convert_operators(f)
    f = add_space(f)
    cl_num = f.count(')')
    op_num = f.count('C') + f.count('A') + f.count('K') + f.count('E')
    if cl_num < op_num:
        f = f'( {f})'
    return f


def check_parenthesis(f):
    """the function verifies whether the lay-out of the parenthesis in the formula is correct"""
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
    """the function converts a raw formula f into a formula in the Reverse Polish Notation"""
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

