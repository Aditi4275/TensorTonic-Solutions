import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.asarray(param)
    grad = np.asarray(grad)
    m = np.asarray(m)
    v = np.asarray(v)
    
    m1 = beta1*m + (1-beta1)*grad
    v1 = beta2*v + (1-beta2)*(grad**2)
    mb = m1/(1-beta1**t)
    vb = v1/(1-beta2**t)

    param_new = param-lr*mb/(np.sqrt(vb)+eps)
    return param_new, m1, v1
    
    pass