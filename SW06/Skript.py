# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:42:04 2019

@author: flori
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04,
79.97, 80.05, 80.03, 80.02, 80.00, 80.02])
print(methodeA.mean())
print(methodeA.std())



##########################

from scipy.stats import norm
np.random.seed(1)
methodeA_sim1 = Series(np.round(norm.rvs(size=6, loc=80, scale=0.02), 2))
methodeA_sim1
methodeA_sim1.mean()
methodeA_sim1.std()
