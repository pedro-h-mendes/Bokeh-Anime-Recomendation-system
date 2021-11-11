from sklearn.neighbors import NearestNeighbors
import numpy as np 
import pandas as pd 
import pickle
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("index", type=int)
#args = parser.parse_args()

# Função para gerar recomendações com base no KNN
def carregar_recomendacao(index):
	anime = pd.read_csv('anime.csv')
	anime_one_hot = pd.read_csv('anime_one_hot.csv',index_col='anime_id')
	loaded_model = pickle.load(open('recomendacao_model.sav', 'rb'))
	teste = np.array(anime_one_hot.loc[index]).reshape(1,50)
	recomendados = loaded_model.kneighbors(teste, return_distance=False).flatten()
	temp = anime[anime['anime_id'].isin(anime_one_hot.index.values[recomendados])]
	temp.columns = ['anime_id', 'Nome', 'Genero', 'Tipo', 'Episódios', 'Nota', 'N° Membros']
	temp = temp[temp['anime_id'] != index]
	return temp

# Função para retornar o anime_id do anime selecionado
def procura_anime_id(input_anime):
    anime = pd.read_csv('anime.csv')
    id_anime = int(anime[anime['name'] == f'{input_anime}'].iloc[:,0])
    return id_anime
