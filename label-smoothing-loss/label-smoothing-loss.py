import math
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    k = len(predictions)
    q = []
    for i in range(k):
        if i == target:
            j = (1-epsilon)+(epsilon/k)
        else:
            j = epsilon/k
        q.append(j)

    loss = 0.0
    for i in range(k):
        loss -= q[i] * math.log(predictions[i])
    return loss