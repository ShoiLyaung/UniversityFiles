import pandas as pd
import numpy as np

def normal_dist(x , mean , sd):
    prob_density = (1/sd*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density