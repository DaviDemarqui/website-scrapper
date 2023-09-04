import os
import random
import time
import csv

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# imports de bibliotecas

def salvar_dados_em_csv(carro):
    arquivo_csv = "dataset_fichas.csv"

    arquivo_existe = os.path.exists(arquivo_csv)

    with open(arquivo_csv, mode='a', newLine='') as file:
        fieldnames = carro.__dict__.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not arquivo_existe:
            writer.writeheader()

        writer.writerow(vars(carro))


# Configurando modelo carro
class FichaTecnicaCarro:
    def __init__(self, marca='', modelo='', ano='0', motor='', tipo='',
                 valvulas='', alimentacao='', posicao='', combustivel='',
                 potencia_cv='0', cilindradas='0', torque='0',
                 direcao='', tracao='', transmissao='',
                 velocidade_max='0', _0_100='0', consumo_cidade='0',
                 consumo_estrada='0', suspensao_dianteira='',
                 suspensao_traseira='', freio_dianteiro='',
                 freio_traseiro='', roda='', pneu='', comprimento='0',
                 entre_eixos='0', altura='0', largura='0', peso='0',
                 carga_util='0', porta_malas='0', tanque='0',
                 portas='0', foto=''):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.tipo = tipo
        self.valvulas = valvulas
        self.alimentacao = alimentacao
        self.posicao = posicao
        self.combustivel = combustivel
        self.potencia_cv = potencia_cv
        self.cilindradas = cilindradas
        self.torque = torque
        self.direcao = direcao
        self.tracao = tracao
        self.transmissao = transmissao
        self.velocidade_max = velocidade_max
        self._0_100 = _0_100
        self.consumo_cidade = consumo_cidade
        self.consumo_estrada = consumo_estrada
        self.suspensao_dianteira = suspensao_dianteira
        self.suspensao_traseira = suspensao_traseira
        self.freio_dianteiro = freio_dianteiro
        self.freio_traseiro = freio_traseiro
        self.roda = roda
        self.pneu = pneu
        self.comprimento = comprimento
        self.entre_eixos = entre_eixos
        self.altura = altura
        self.largura = largura
        self.peso = peso
        self.carga_util = carga_util
        self.porta_malas = porta_malas
        self.tanque = tanque
        self.portas = portas
        self.foto = foto


#  Botando pra escaralhar
def escaralhando(url):
    request_header = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/78.0.3904.70 Safari/537.36",
        "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    ]

    print("Start scrapping page: " + url)

    # Realizando a solicitação HTTP para a pagina
    headers = {
        'User-Agent': random.choice(request_header)
    }

    dr = webdriver.Chrome()
    dr.get(url)
    response = dr.page_source
    soup = BeautifulSoup(response, 'html.parser')

    select_element_ano = soup.find('select', id='ano')
    select_element_versao = soup.find('select', id='versao')

    if select_element_ano and select_element_versao:
        selected_option_ano = select_element_ano.find('option', selected=True)
        selected_option_versao = select_element_versao.find('option', selected=True)

        if selected_option_ano and selected_option_versao:
            carro_ano = selected_option_ano.text.strip()
            carro_versao = selected_option_versao.text.strip()

    titulo_para_atributo = {
        'Ano': 'ano',
        'Motorização': 'motor',
        'Tipo': 'tipo',
        'Valvulas': 'valvulas',
        'Alimentação': 'alimentacao',
        'Posição': 'posicao',
        'Combustível': 'combustivel',
        'Potência (cv)': 'potencia_cv',
        'Cilindradas': 'cilindradas',
        'Torque (Kgf.m)': 'torque',
        'Direção': 'direcao',
        'Tração': 'tracao',
        'Transmissão': 'transmissao',
        'Velocidade máx (Km/h)': 'velocidade_max',
        'Tempo 0-100Km/h': '_0_100',
        'Consumo cidade (Km/L)': 'consumo_cidade',
        'Consumo estrada (Km/L)': 'consumo_estrada',
        'Suspensão Dianteira': 'suspensao_dianteira',
        'Suspensão Traseira': 'suspensao_traseira',
        'Freio dianteiro': 'freio_dianteiro',
        'Freio traseiro': 'freio_traseiro',
        'Roda': 'roda',
        'Pneu': 'pneu',
        'COMPRIMENTO': 'comprimento',
        'ENTRE-EIXOS': 'entre_eixos',
        'ALTURA': 'altura',
        'LARGURA': 'largura',
        'PESO EM ORDEM DE MARCHA': 'peso',
        'Carga Útil': 'carga_util',
        'PORTA-MALAS': 'porta_malas',
        'TANQUE': 'tanque',
        'Portas': 'portas',
        'Foto': 'foto',
    }

    carro = FichaTecnicaCarro()

    tr_tags = soup.find_all('tr')

    for tr in tr_tags:
        td_tags = tr.find_all('td')
        if len(td_tags) >= 2:
            titulo = td_tags[0].text.strip()
            valor = td_tags[1].text.strip()

            # Verificando se to titulo esta mapeado para um atribuido do objeto
            if titulo in titulo_para_atributo:
                atributo = titulo_para_atributo[titulo]
                setattr(carro, atributo, valor)
        print(carro)

    carro.marca = 'Honda'
    carro.ano = carro_ano
    carro.modelo = carro_versao

    # Criando .CSV com os dados salvos!
    # salvar_dados_em_csv(carro)
    print(carro)


def main():
    urls = ['https://www.shopcar.com.br/fichatecnica.php?id=3655']  # Link de teste!

    total_urls = len(urls)
    scrap_time = 0
    for i, url in enumerate(urls):
        print('Scraping URL {} of {}: {}'.format(i + 1, total_urls, url))
        # Perform scraping and saving to the database here (e.g., escaralhando(url))
        escaralhando(url)
        scrap_time += 1

        if scrap_time % 2 == 0 and scrap_time < total_urls:
            print("Waiting for 60 seconds...")
            time.sleep(60)  # Wait for 60 seconds every 2 scrapes

    print("Scraping complete for all {} URLs.".format(total_urls))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
