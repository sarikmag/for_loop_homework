def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    n=len(list1)
    r=[]
    for i in range(n):
        r+=[list1[i].capitalize()]
    return r
print(main(("rustam","diyor","bektosh")))