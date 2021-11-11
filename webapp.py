#------------------BIBLIOTECAS------------------#
from bokeh.layouts import row, column, widgetbox
from bokeh.models import TextInput, Button,  Div
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn
from bokeh.models.widgets import AutocompleteInput
from bokeh.plotting import curdoc
import pandas as pd
import numpy as np

from recomendacao_lib import carregar_recomendacao, procura_anime_id
#------------------BIBLIOTECAS------------------#

#--------------------DATASET--------------------#
anime = pd.read_csv('anime.csv')
#--------------------DATASET--------------------#

#--------------FUNÇÃO-RECOMENDAÇÃO--------------#
def recomendacao_animes():

  id_anime = procura_anime_id(entrada_anime.value) # retorna o anime_id do nome do anime selecionado
  recomendacoes = carregar_recomendacao(id_anime) # aplica a função de recomendação com base no KNN

  try:

    Columns = [TableColumn(field=Ci, title=Ci) for Ci in recomendacoes.columns] # bokeh columns
    data_table = DataTable(columns=Columns, source=ColumnDataSource(recomendacoes)) # bokeh table

    # Layout
    table = column(data_table)
    curdoc().add_root(table)

  # Tratamento de erros
  except KeyboardInterrupt:
    return 
  except ValueError as e:
    div_widget.text = f'<h2>Um erro ocorreu: {str(e)}</h2>'
  except Exception as e:
    errMsg = f'<h2>Ocorreu um erro inesperado com a mensagem de erro: {str(e)}<br>'
    div_widget.text = errMsg
#--------------FUNÇÃO RECOMENDAÇÃO--------------#

#---------------------LAYOUT--------------------#
div_widget = Div(text="Sistema de Recomendação de Animes", width=400, height=20) # title

# Caixa de entrada com autocomplete dos animes listados no dataset
entrada_anime = AutocompleteInput(title='Coloque aqui um anime que você goste', completions=anime['name'].tolist(), case_sensitive=False, value='')

# Botão
button_widget = Button(label='Buscar Recomendações', button_type='success')
button_widget.on_click(recomendacao_animes)

controls = column([entrada_anime, button_widget], width=245)

layout = row(column(div_widget, controls))
#--------------------LAYOUT--------------------#

#-------------------DOCUMENT-------------------#
curdoc().add_root(layout)
curdoc().title = 'Recomendação de Animes'
#-------------------DOCUMENT-------------------#