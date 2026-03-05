def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    rank = {category: rank for rank, category in enumerate(ordering)}

    encoded = [rank[v]  for v in values]

    return encoded