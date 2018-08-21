# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:47:12 2018

@author: jeffe
"""

def primeirafuncao():
    print('hi word')
    
def primeirafuncao(nome):
    print('hi {}'.format(nome))
    
def printVarInfo(arg1, *vart):
    print('o parametro passdo foi ', arg1)
    
    for item in vart:
        print('o parametro passsado foi: ',item)
        
potencia = lambda num: num**2

        
