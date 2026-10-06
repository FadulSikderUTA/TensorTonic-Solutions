import numpy as np
import math
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    na, nb = np.linalg.norm(a), np.linalg.norm(b)

    if na == 0 or nb == 0:
        return 0.0
    
    return float(np.dot(a,b)/(na*nb))