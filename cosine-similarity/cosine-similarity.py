import numpy as np
import math
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    norm_a = 0
    norm_b = 0
    dot_ab = 0
    result = 0
    for i in range(len(a)):
        norm_a += a[i]*a[i]
        norm_b += b[i]*b[i]
        dot_ab += a[i]*b[i]


    if norm_a!=0 and norm_b !=0:
        result = dot_ab/(math.sqrt(norm_a)*math.sqrt(norm_b))

    
    return float(result)