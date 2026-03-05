def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    unique = {item for sublist in recommendations for item in sublist}
    
    return len(unique)/n_items