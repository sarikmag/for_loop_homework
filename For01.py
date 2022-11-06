import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    r=[]
    for i in range(n):
        r.append(i)
    return r
print(main(5))