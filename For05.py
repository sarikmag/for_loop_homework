def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    r=[]
    for i in range(B,A-1,-1):
        r.append(i)
    return r
print(main(5,9))