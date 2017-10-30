def distance(strand_a, strand_b):
    """"""
    return sum(1 for a,b in zip(strand_a, strand_b) if a != b)