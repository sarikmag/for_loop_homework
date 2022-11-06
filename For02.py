def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    r=""
    for i in range(n):
        if i>0 and i!=n:
            r+=","
        r+=(str(i))
    
    return r
print(main(3))