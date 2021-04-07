# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:46:02 2021

@author: denis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


base = pd.read_csv('INFLUD21-29-03-2021.csv', sep=";",low_memory = False)
#dados faltantes por coluna no CSV todo
dados_nulos_base = base.isnull().sum()
dados_nulos_base.plot()

# COMO TEMOS UMA BASE DE DADOS EXTENSA, VAMOS SEPARAR O DOCUMENTO EM VARIAVEIS PARA ANALISAR O QUE REALMENTE FOR NECESSARIO 

nova_base = base.head(100)

#dados_nulos = nova_base.isnull().sum().plot()
dados_nulos = nova_base.isnull().sum().plot()
dados_nulos.plot()

nova_base.info()
