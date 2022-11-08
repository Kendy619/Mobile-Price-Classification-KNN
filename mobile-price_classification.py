# -*- coding: utf-8 -*-
"""IA_Ex09_KNN_Pacientes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Kendy619/Classificador-KNN/blob/main/IA_Ex09_KNN_Pacientes.ipynb

# Treinamento

### Carregando Arquivo de Treinamento (.csv)
"""

import pandas as pd
# Carregando dados do arquivo CSV
url = 'https://raw.githubusercontent.com/Kendy619/Mobile-Price-Classification-KNN/main/train.csv'
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'latin1').values
print("--------------------------------------------------------")
print("Dados dos celulares - TREINAMENTO - Dimensão ",base_Treinamento)
print("--------------------------------------------------------")
print(base_Treinamento[:,:])
print("---------------------------------")

# Extração dos Atributos a serem utilizadas pela rede
print("Atributos de Entrada")
print("---------------------------------")
print(base_Treinamento[:, :20])

print("----------------------------")
print("Classificação Supervisionada")
print("----------------------------")
print(base_Treinamento[:, 20])

"""### Pré-processamento de Dados"""

import numpy as np 
from sklearn import preprocessing

# Binarizador de rótulo
min_max = preprocessing.MinMaxScaler()
atributos_normalizados = min_max.fit_transform(base_Treinamento[:,:20])


print("--------------------------------")
print("Atributos de Entrada - Numéricos")
print("--------------------------------")
print(atributos_normalizados)

print("----------------------------------------")
print("Classificação Supervisionada - Numéricos")
print("----------------------------------------")
diagnostico_normalizados = base_Treinamento[:,20]
print(diagnostico_normalizados)

"""### Treinamento do KNN (K-Nearest Neighbor)"""

from sklearn.neighbors import KNeighborsClassifier
# Treinamento do Knn a partir dos atributos de entrada e classificações com K=3
modelo = KNeighborsClassifier(n_neighbors=2000)
modelo.fit(atributos_normalizados, diagnostico_normalizados)

# Acurácia do modelo, que é : 1 - (predições erradas / total de predições)
# Acurácia do modelo: indica uma performance geral do modelo. 
# Dentre todas as classificações, quantas o modelo classificou corretamente;
# (VP+VN)/N
print('Acurácia: %.4f' % modelo.score(atributos_normalizados, diagnostico_normalizados))

"""### ----------------------------------------------------------------------------

# Validação do Aprendizado

### Predição Simples
"""

Iphone13 = [[3240,1,2.0,1,12,1,512,1.6,174,6,12,1170,2532,3857,19,9,15,1,1,1]]
print("Iphone13", modelo.predict(Iphone13))
PocoX3 = [[5000,1,3.0,1,48,1,256,2.0,250,8,32,1080,2400,10240,19,9,32,1,1,1]]
print("PocoX3", modelo.predict(PocoX3))

"""### Predição a partir de base de dados (.csv)"""

import pandas as pd
# Carregando dados do arquivo CSV
url = 'https://raw.githubusercontent.com/Kendy619/Mobile-Price-Classification-KNN/main/test.csv'
base_Testes = pd.read_csv(url,sep=',', encoding = 'latin1').values
print("----------------------------")
print("Dados dos Pacientes - TESTES")
print("----------------------------")
print(base_Testes)
print("---------------------------------")

# Extração dos Atributos a serem utilizadas pela rede
print("Atributos de Entrada")
print("---------------------------------")
print(base_Testes[:, 0:20])

"""### Pré-processamento de Dados"""

import numpy as np 
from sklearn import preprocessing

atributos_normalizados = min_max.transform(base_Testes[:,:20])
print("--------------------------------")
print("Atributos de Entrada - Numéricos")
print("--------------------------------")
print(atributos_normalizados)

"""### Predição da Base"""

base_Predicao = modelo.predict((atributos_normalizados))
print("Classificações: ", base_Predicao)