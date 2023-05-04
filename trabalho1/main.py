import pandas as pd
import numpy as np

data = pd.read_csv('trabalho1/base_nba_final.csv', header=(0))

data = data.drop(['Unnamed: 0'], axis=1)

data = data.drop(['Match Up', 'a.Match Up', 'Game Date', 'a.Game Date', '+/-', 'a.+/-'], axis=1)

dfNome = data[['Team', 'a.Team']]

data = data.drop(['Team', 'a.Team'], axis=1)

data2 = pd.DataFrame(columns=list(['Home', 'Away']))
for i in range(data.shape[0]):
  if data['W/L'][i] == "W" and data['a.W/L'][i] == "L":
    data2.loc[i] = [1,0]
  elif data['W/L'][i] == "L" and data['a.W/L'][i] == "W":
    data2.loc[i] = [0,1]
  else:
    data2.loc[i] = [9,9]
    
data = data.drop(['W/L', 'a.W/L'], axis=1)
data = data.drop(['PTS', 'a.PTS'], axis = 1)

for column in data:
    try:
        if data[column].max() < 1:
            data[column] = data[column] / 1
        elif data[column].max() < 10:
            data[column] /= 10
        elif data[column].max() < 100:
            data[column] /= 100
        elif data[column].max() < 1000:
            data[column] /= 1000
        elif data[column].max() < 10000:
            data[column] /= 10000
        elif data[column].max() < 100000:
            data[column] /= 100000
        elif data[column].max() < 1000000:
            data[column] /= 1000000
        else:
            print('Erro')
    except:
        print('Exception')

print(data)

data = data.replace('?', np.nan)
data = data.dropna()
X = np.array(data[data.columns[0:data.shape[1]-1]], dtype=float)
medias = np.nanmean(X, axis=0)
for i in np.arange(0, X.shape[0]):
  for j in np.arange(0, X.shape[1]):
    if (np.isnan(X[i,j])== True):
      X[i,j] = medias[j]
      
print(X)