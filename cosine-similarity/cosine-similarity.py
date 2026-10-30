import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    numerator = float(np.dot(a, b))
    norm_a = float(np.linalg.norm(a))
    norm_b = float(np.linalg.norm(b))
    

    if norm_a == 0 or norm_b == 0:
        return 0.0

    denominator = norm_a * norm_b
    return numerator / denominator