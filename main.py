import requests
from bs4 import BeautifulSoup
import mysql.connector
# imports de bibliotecas

import carro

# Configurando banco de dados
db_config = {
    'host': 'localhost:3306',
    'user': 'root',
    'password': '010203',
    'database': 'monaco'
}


def main():
    urls = ['https://www.fichacompleta.com.br/carros/volkswagen/passat-variant-2-0-tsi-2013'] # Link de teste!


    for url in urls:
        print("Start scrapping page: " + url)

        # Realizando a solicitação HTTP para a pagina
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Encontrando todos os elementos com a classe "colEsq"
            # Geralmente são titulos como ex: Marca, Combustivel etc...
            col_esq_elements = soup.find_all('div', class_='colEsq')

            # Dicionario de pares de valores
            valores = {}

            for col_esq in col_esq_elements:
                chave = col_esq.get_text(strip=True)

                valor = col_esq.find_next_sibling('div', class_='colDir').get_text(strip=True)

                # Armazenando o par chave-valor no dicionario
                valores[chave] = valor

            for chave, valor in valores.items():
                print(f"{chave}: {valor}")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
