def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    if a>0 or a==0:
        return True
    if a<0:
        return False 
print(main(0))