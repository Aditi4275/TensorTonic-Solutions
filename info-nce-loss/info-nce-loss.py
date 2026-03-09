import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    Z1 = np.asarray(Z1)
    Z2 = np.asarray(Z2)
    
    
    logits = np.dot(Z1, Z2.T) / temperature
    
    
    logits_max = np.max(logits, axis=1, keepdims=True)
    
    logits_stable = logits - logits_max
    
   
    pos = np.diag(logits_stable) 

    exp_logits = np.exp(logits_stable)
    sum_exp = np.sum(exp_logits, axis=1)
    
    
    log_prob = pos - np.log(sum_exp)

    return -np.mean(log_prob)