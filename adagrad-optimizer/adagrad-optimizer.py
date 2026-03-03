import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w = np.asarray(w)
    g = np.asarray(g)
    G = np.asarray(G)
    
    Gt = G + (g**2)
    p = lr/(np.sqrt(Gt + eps))
    wt = w - p*g

    return wt, Gt