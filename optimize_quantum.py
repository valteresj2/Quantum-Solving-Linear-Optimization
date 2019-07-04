# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:08:07 2019

@author: valter.e.junior
"""

import pandas as pd
import numpy as np


class optimize_quantum(object):
    
    def product_notable(A_eq,b_eq,var):
        contrainst=[]
        features=[]
        for index,k in enumerate(A_eq):
            var1=pd.Series(var)
            map_p=list(var1[np.where(np.array(k)!=0)[0]])
            g=list(pd.Series(k)[np.where(np.array(k)!=0)[0]])
            g.append(b_eq[index]*-1)
            map_p.append('c')
            g1=[]
            tipo=[]
            for i in range(len(g)):
                for j in range(len(g)):
                    g1.append(g[i]*g[j])
                    if i==j and map_p[i]!='c':
                        tipo.append(map_p[i])
                    elif i!=j and map_p[i]=='c' and map_p[j]!='c':
                        tipo.append(map_p[j])
                    elif i!=j and map_p[i]!='c' and map_p[j]=='c':
                        tipo.append(map_p[i])
                    else:
                        value=[map_p[i],map_p[j]]
                        value.sort()
                        value='||'.join(value)
                        tipo.append(value)
                
            
            
            g1=pd.Series(g1)  
            cont=0
            dt=pd.DataFrame({'var':tipo,'value':g1}).groupby('var').sum()
            value=list(dt['value'])
            maping=list(dt.index)
            
  
            contrainst.extend(value)
            features.extend(maping)
            print(index)
            
    
        dt=pd.DataFrame({'var':features,'value':contrainst}).groupby('var').sum()
        value=list(dt['value'])
        maping=list(dt.index)

         
        
        if value.count(0)>0:
           value=list(pd.Series(value)[np.where(np.array(value)!=0)[0]])
           maping=list(pd.Series(maping)[np.where(np.array(value)!=0)[0]])
        return maping,value


    def model_dwave(maping,value,const=False):
        Q={}
        if const==False:
            index=np.where(np.array(maping)=='c||c')[0][0]
            maping.pop(index)
            value.pop(index)
        for i,values in enumerate(maping):
            if values.count('||')==1:
                Q[(values[0:values.find('||')],values[values.find('||')+2:len(values)])]=value[i]
            else:
                Q[(values,values)]=value[i]
        return Q
    
    def result_dwave(response,var,dtype='max',fgoal=[]):
        amostras=[]
        energy=[]
        occurences=[]
        
        for datum in response.data(['sample', 'energy', 'num_occurrences']):
            amostras.append(datum.sample)
            energy.append(datum.energy)
            occurences.append(datum.num_occurrences)
        
        data={}
        data['samples']=amostras
        data['energy']=energy
        data['ocurrences']=occurences
        data=pd.DataFrame(data)
        data=data[data['energy']==min(data['energy'])]
        #data=data[data['ocurrences']==max(data['ocurrences'])]
        value=[]
        for i in range(len(data)):
            data1=data.iloc[i,:]
            data1=data1['samples']
            index=[]
            
            for j in list(data1.keys()):
                index.append(np.where(np.array(var)==j)[0][0])
            value.append(np.dot(np.array(list(data1.values())),np.array(fgoal)[index]))
        if dtype=='max':
            data1=data.iloc[np.where(np.array(value)==max(value))[0][0],:]
        else:
            data1=data.iloc[np.where(np.array(value)==min(value))[0][0],:]
        data1=data1['samples']
        data1=pd.DataFrame({'Variavel':list(data1.keys()),'value':list(data1.values())})
            
            
            
        return data1
