# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:47:32 2019

@author: flori
"""

##########################################################################

from scipy.stats import norm, binom

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

zufallsZahlen = st.norm.rvs(size=10)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.norm.rvs(size=20)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.norm.rvs(size=50)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.norm.rvs(size=100)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.t.rvs(size=100, df=20)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.t.rvs(size=100, df=7)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.t.rvs(size=100, df=3)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.t.rvs(size=20, df=20)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.t.rvs(size=20, df=7)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.t.rvs(size=20, df=3)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.chi.rvs(size=100, df=20)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.chi.rvs(size=100, df=7)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.chi.rvs(size=100, df=3)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.chi.rvs(size=20, df=20)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.chi.rvs(size=20, df=7)
st.probplot(zufallsZahlen, plot=plt)

zufallsZahlen = st.chi.rvs(size=20, df=3)
st.probplot(zufallsZahlen, plot=plt)
