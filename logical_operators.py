
def neg_op(b):
    return 1 - int(b)


def or_op(b_1, b_2):
    return max(int(b_1), int(b_2))


def and_op(b_1, b_2):
    return min(int(b_1), int(b_2))


def imp_op(b_1, b_2):
    return max(1-int(b_1), int(b_2))


def eqv_op(b_1, b_2):
    return 1 if b_1 == b_2 else 0

