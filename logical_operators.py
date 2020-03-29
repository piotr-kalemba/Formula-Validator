
def neg_op(b):
    """the function returns boolean value of negation"""
    return 1 - b


def or_op(b_1, b_2):
    """the function returns boolean value of disjunction"""
    return max(b_1, b_2)


def and_op(b_1, b_2):
    """the function returns boolean value of conjunction"""
    return min(b_1, b_2)


def imp_op(b_1, b_2):
    """the function returns boolean value of conditional"""
    return max(1-b_1, b_2)


def eqv_op(b_1, b_2):
    """the function returns boolean value of biconditional"""
    return 1 if b_1 == b_2 else 0

