def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    sums = {}
    counts = {}

    for cat, target in zip(categories, targets):
        sums[cat] = sums.get(cat, 0) + target
        counts[cat] = counts.get(cat, 0) + 1
    means = {}

    for cat in sums:
        means[cat] = sums[cat]/counts[cat]

    op = [means[cat] for cat in categories]

    return op