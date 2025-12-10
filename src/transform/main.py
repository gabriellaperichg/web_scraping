import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../data/data.jsonl', lines=True)

# mostrar todas as colunas da tabela
# pd.options.display.max_columns = None

# adiciona a coluna de data source
df['source'] = 'https://www.amazon.com.br/s?i=stripbooks&rh=n%3A6740748011%2Cp_36%3A-2200%2Cp_n_feature_nine_browse-bin%3A8529758011%2Cp_n_condition-type%3A13862762011&dc&qid=1765039756&rnid=13862761011&ref=sr_nr_p_n_condition-type_1&ds=v1%3AzM0bfKZhUGrxmjDqR%2BjeG44Ecn1kvzp4NOZrNlcRAqI'

# data da coleta
df['colectDate'] = datetime.now()

df = df.fillna(0)

# conectar ao SQLite (ou criar um novo)
conn = sqlite3.connect('../data/quotes.db')

# salvar o df no db
df.to_sql('amazon', conn, if_exists='replace', index=False)

# fechar conexão
conn.close()