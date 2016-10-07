#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def caja_negra (x):

    d = np.size(x)
    result = 0

    for ii in range (d):
        result += x[ii]**3 - 16*x[ii]**2 + 5*x[ii]

    return 0.5*np.sqrt(np.abs(result)) - x[ii] + 4.856777

def bohachevski (x):

    term1 = x[0]**2
    term2 = 2*x[1]**2
    term3 = -0.3 * np.cos(3*np.pi*x[0])
    term4 = -0.4 * np.cos(4*np.pi*x[1])

    return term1 + term2 + term3 + term4 + 0.7

    
def goldstein_price(x):
    
    fact1a = (x[0] + x[1] + 1)**2
    fact1b = 19 - 14*x[0] + 3*x[0]**2 - 14*x[1] + 6*x[0]*x[1] + 3*x[1]**2
    fact1 = 1 + fact1a*fact1b

    fact2a = (2*x[0] - 3*x[1])**2
    fact2b = 18 - 32*x[0] + 12*x[0]**2 + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2
    fact2 = 30 + fact2a*fact2b

    return fact1*fact2

def easom(x):

    fact1 = -np.cos(x[0])*np.cos(x[1])
    fact2 = np.exp(-(x[0]-np.pi)**2-(x[1]-np.pi)**2)

    return fact1*fact2;

def eggholder(x):

    term1 = -(x[1]+47) * np.sin(np.sqrt(abs(x[1]+x[0]/2+47)))
    term2 = -x[0] * np.sin(np.sqrt(abs(x[0]-(x[1]+47))))

    return term1 + term2