
def neg_op(b):
    return 1 - b


def or_op(b_1, b_2):
    return max(b_1, b_2)


def and_op(b_1, b_2):
    return min(b_1, b_2)


def imp_op(b_1, b_2):
    return max(1-b_1, b_2)


def eqv_op(b_1, b_2):
    return 1 if b_1 == b_2 else 0

