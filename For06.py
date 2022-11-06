def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    r=0
    for i in range(A,B):
        r+=i
    return r
print(main(-6,8))