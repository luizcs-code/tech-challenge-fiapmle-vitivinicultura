import pandas as pd
import requests
from app.sql_app.database_manager import DatabaseManager
from app.config import settings_data_processing
import os


class ComercDataCSV:
    def __init__(self):
        # Configurações iniciais: obtenção da URL e caminho do arquivo CSV a partir de um arquivo de configuração centralizado.
        self.csv_url = settings_data_processing['Comercializacao']['url']
        self.csv_path = settings_data_processing['Comercializacao']['CSV']
        # Criação de uma instância do gerenciador de banco de dados.
        database_path = settings_data_processing['database_path']  
        self.db_manager = DatabaseManager(database_path)
        # Configuração e verificação da existência da tabela no banco de dados.
        self.setup_database()

    def setup_database(self):
        # Schema da tabela Comercializacao. Certifica-se de que a tabela exista antes de tentar carregar dados nela.
        schema = "CREATE TABLE IF NOT EXISTS Comercializacao (produto TEXT, quantidade REAL)"
        self.db_manager.create_table_if_not_exists("Comercializacao", schema)

    async def download_csv(self):
        # Download do arquivo CSV usando a biblioteca requests.
        response = requests.get(self.csv_url)
        with open(self.csv_path, 'wb') as f:
            f.write(response.content)
        print("Arquivo baixado com sucesso.")

    async def process_csv(self):
        # Carregamento e processamento do CSV: remoção de uma coluna indesejada.
        data = pd.read_csv(self.csv_path, delimiter=';')
        data.drop(columns=data.columns[1], inplace=True)
        return data

    async def load_into_database(self):
        # Carregamento dos dados processados para a tabela no banco de dados.
        data = await self.process_csv()
        self.db_manager.load_data(data, 'Comercializacao')
        print("Dados carregados no banco de dados com sucesso.")

    async def delete_csv_after_use(self):
        # Remoção do arquivo CSV após o uso para evitar desordem e uso de espaço desnecessário.
        
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
            print("Arquivo CSV removido após o uso.")

