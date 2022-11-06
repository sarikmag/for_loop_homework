def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    r=[]
    for i in range(10):
        if i>0:
            r.append(i*price)
    return r
price(main(2.25))