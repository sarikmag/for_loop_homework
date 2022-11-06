def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    r=0
    for i in range(4):
        if i>0:
            r+=(1/i)
    return r
print(main(4))