# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:10:32 2019

@author: valter.e.junior
"""

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())

import pandas as pd
import numpy as np
from scipy.optimize import linprog
from optimize_quantum import optimize_quantum


A_eq=[]    
b_eq=[] 

A_eq.append([1,0,1])
A_eq.append([0,1,1])
b_eq=[1,1]

var=['x1','x2','x3']
c=[7,4,19]

identy=np.identity(len(A_eq),dtype='int')
for i in range(len(A_eq)):
    c.append(0)
    var.append('AUX_'+str(i))
    A_eq[i].extend(list(identy[i]))
    


res = linprog([-i for i in c],A_eq=A_eq, b_eq=b_eq,
bounds=(0, 1))

print('Optimal value:', res.fun, '\nX:', res.x)

result_simplex=pd.DataFrame({'Variavel':var,'value':res.x})



result=optimize_quantum.product_notable(A_eq,b_eq,var)
Q=optimize_quantum.model_dwave(result[0],result[1])


response = sampler.sample_qubo(Q, num_reads=1000)

result_dwave=optimize_quantum.result_dwave(response,var=var,dtype='max',fgoal=c)
