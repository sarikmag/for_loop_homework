def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    r=[]
    for i in range(A,B+1):
        r.append(i)
    return r
print(main(2,7))