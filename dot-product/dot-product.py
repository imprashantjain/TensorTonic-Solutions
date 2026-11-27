import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    size=len(x);
    ans=0;
    for i in range(0,size):
        ans+=x[i]*y[i];
    return ans
    