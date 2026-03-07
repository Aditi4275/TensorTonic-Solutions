import numpy as np 

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    points = np.asarray(points)
    assignments = np.asarray(assignments)
    num_dmis = points.shape[1]
    centroids = np.zeros((k, num_dmis))

    for i in range(k):
        cluster_points = points[assignments == i]

        if len(cluster_points) > 0:
            centroids[i] = cluster_points.mean(axis = 0)
        else:
            centroids[i] = np.zeros(num_dmis)

    return centroids.tolist()