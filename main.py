import csv
import random
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# imports de bibliotecas

lista_de_carros = []
nome_arquivo = 'ficha_carros_database.csv'


def alternative_key(dictionary, key, alternate_key1, alternate_key2):
    try:
        return dictionary[key]
    except KeyError:
        try:
            return dictionary[alternate_key1]
        except KeyError:
            try:
                return dictionary[alternate_key2]
            except KeyError:
                return "N/D"


def salvar_dados_em_csv(lista_de_carros, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Escreva os dados dos carros com instruções SQL INSERT
        for carro in lista_de_carros:
            insert_sql = (
                'INSERT INTO `karangoo`.`ficha_carros` (`marca`, `modelo`, `ano`, `combustivel`, `configuracao`, '
                '`garantia`, `geracao`, `lugares`, `plataforma`, `portas`, `porte`, `procedencia`, '
                '`aceleracao_0_100`, `velocidade_maxima`, `acoplamento`, `cambio`, `codigo_cambio`, '
                '`quantidade_marchas`, `tracao`, `alimentacao`, `aspiracao`, `cilindros`, '
                '`codigo_motor`, `comando_valvulas`, `curso_pistao`, `diametro_cilindro`, `disposicao`, `instalacao`, '
                '`peso_potencia`, `peso_torque`, `potencia_especifica`, `potencia_G`, `potencia_A`, `potencia_maxima`, `razao_compressao`, '
                '`torque_especifico`, `torque_A`, `torque_G`, `torque_maximo`, `tuchos`, `valvulas_por_cilindro`, `variacao_comando`, '
                '`altura`, `bitola_dianteira`, `bitola_traseira`, `carga_util`, `comprimento`, `distancia_eixos`, '
                '`largura`, `peso`, `porta_malas`, `tanque_combustivel`, `freios_dianteiros`, `freios_traseiros`, '
                '`assistencia`, `suspensao_dianteira`, `elemento_elastico`, `suspensao_traseira`, '
                '`consumo_rodoviario_A`, `consumo_rodoviario_G`, `consumo_rodoviario_D`, `consumo_urbano_A`, '
                '`consumo_urbano_G`, `consumo_urbano_D`) VALUES(')
            insert_sql += f"'{carro.marca}', '{carro.modelo}', '{carro.ano}', '{carro.combustivel}', '{carro.configuracao}', '{carro.garantia}', '{carro.geracao}', '{carro.lugares}', '{carro.plataforma}', '{carro.portas}', '{carro.porte}', '{carro.procedencia}', '{carro.aceleracao_0_100}', '{carro.velocidade_maxima}', '{carro.acoplamento}', '{carro.cambio}', '{carro.codigo_cambio}', '{carro.quantidade_marchas}', '{carro.tracao}', '{carro.alimentacao}', '{carro.aspiracao}', '{carro.cilindros}', '{carro.codigo_motor}', '{carro.comando_valvulas}', '{carro.curso_pistao}', '{carro.diametro_cilindro}', '{carro.disposicao}', '{carro.instalacao}', '{carro.peso_potencia}', '{carro.peso_torque}', '{carro.potencia_especifica}', '{carro.potencia_G}', '{carro.potencia_A}', '{carro.potencia_maxima}', '{carro.razao_compressao}', '{carro.torque_especifico}', '{carro.torque_A}', '{carro.torque_G}', '{carro.torque_maximo}', '{carro.tuchos}', '{carro.valvulas_por_cilindro}', '{carro.variacao_comando}', '{carro.altura}', '{carro.bitola_dianteira}', '{carro.bitola_traseira}', '{carro.carga_util}', '{carro.comprimento}', '{carro.distancia_eixos}', '{carro.largura}', '{carro.peso}', '{carro.porta_malas}', '{carro.tanque_combustivel}', '{carro.freios_dianteiros}', '{carro.freios_traseiros}', '{carro.assistencia}', '{carro.suspensao_dianteira}', '{carro.elemento_elastico}', '{carro.suspensao_traseira}', '{carro.consumo_rodoviario_A}', '{carro.consumo_rodoviario_G}', '{carro.consumo_rodoviario_D}', '{carro.consumo_urbano_A}', '{carro.consumo_urbano_G}', '{carro.consumo_urbano_D}'"
            insert_sql += ');'

            # Escreva a instrução SQL INSERT no arquivo CSV
            writer.writerow([insert_sql])


# Configurando modelo carro
class Carro:
    def __init__(self, marca, modelo, ano, combustivel, configuracao, garantia, geracao, lugares, plataforma, portas,
                 porte, procedencia, aceleracao_0_100, velocidade_maxima, acoplamento, cambio, codigo_cambio,
                 quantidade_marchas, tracao, alimentacao, aspiracao, cilindros, codigo_motor,
                 comando_valvulas, curso_pistao, diametro_cilindro, disposicao, instalacao, peso_potencia, peso_torque,
                 potencia_especifica, potencia_G, potencia_A, potencia_maxima, razao_compressao, torque_especifico,
                 torque_A, torque_G, torque_maximo, tuchos, valvulas_por_cilindro,
                 variacao_comando, altura, bitola_dianteira, bitola_traseira, carga_util, comprimento, distancia_eixos,
                 largura, peso, porta_malas, tanque_combustivel, freios_dianteiros, freios_traseiros, assistencia,
                 suspensao_dianteira, elemento_elastico, suspensao_traseira, consumo_rodoviario_A,
                 consumo_rodoviario_G, consumo_rodoviario_D, consumo_urbano_A, consumo_urbano_G, consumo_urbano_D):
        self.marca = marca
        self.modelo = modelo[len(marca) + 1:]
        self.ano = ano
        self.combustivel = combustivel
        self.configuracao = configuracao
        self.garantia = garantia
        self.geracao = geracao
        self.lugares = lugares
        self.plataforma = plataforma
        self.portas = portas
        self.porte = porte
        self.procedencia = procedencia
        self.aceleracao_0_100 = aceleracao_0_100
        self.velocidade_maxima = velocidade_maxima
        self.acoplamento = acoplamento
        self.cambio = cambio
        self.codigo_cambio = codigo_cambio
        self.quantidade_marchas = quantidade_marchas
        self.tracao = tracao
        self.alimentacao = alimentacao
        self.aspiracao = aspiracao
        self.cilindros = cilindros
        self.codigo_motor = codigo_motor
        self.comando_valvulas = comando_valvulas
        self.curso_pistao = curso_pistao
        self.diametro_cilindro = diametro_cilindro
        self.disposicao = disposicao
        self.instalacao = instalacao
        self.peso_potencia = peso_potencia
        self.peso_torque = peso_torque
        self.potencia_especifica = potencia_especifica
        self.potencia_A = potencia_A
        self.potencia_G = potencia_G
        self.potencia_maxima = potencia_maxima
        self.razao_compressao = razao_compressao
        self.torque_especifico = torque_especifico
        self.torque_A = torque_A
        self.torque_G = torque_G
        self.torque_maximo = torque_maximo
        self.tuchos = tuchos
        self.valvulas_por_cilindro = valvulas_por_cilindro
        self.variacao_comando = variacao_comando
        self.altura = altura
        self.bitola_dianteira = bitola_dianteira
        self.bitola_traseira = bitola_traseira
        self.carga_util = carga_util
        self.comprimento = comprimento
        self.distancia_eixos = distancia_eixos
        self.largura = largura
        self.peso = peso
        self.porta_malas = porta_malas
        self.tanque_combustivel = tanque_combustivel
        self.freios_dianteiros = freios_dianteiros
        self.freios_traseiros = freios_traseiros
        self.assistencia = assistencia
        self.suspensao_dianteira = suspensao_dianteira
        self.elemento_elastico = elemento_elastico
        self.suspensao_traseira = suspensao_traseira
        self.consumo_rodoviario_A = consumo_rodoviario_A
        self.consumo_rodoviario_G = consumo_rodoviario_G
        self.consumo_rodoviario_D = consumo_rodoviario_D
        self.consumo_urbano_A = consumo_urbano_A
        self.consumo_urbano_G = consumo_urbano_G
        self.consumo_urbano_D = consumo_urbano_D


def atualizar_campos_carro(carro):
    if len(carro.torque_maximo) > 9:
        parts = carro.torque_maximo.split('(A)')
        if len(parts) > 1:
            carro.torque_A = parts[0].strip()
            parts_G = parts[1].split('(G)')
            if len(parts_G) > 1:
                carro.torque_G = parts_G[0].strip()
                carro.torque_maximo = "N/D"
        else:
            carro.torque_A = "N/D"
            carro.torque_G = "N/D"

def atualizar_campos_potencia(carro):
    if len(carro.potencia_maxima) > 14:
        parts = carro.potencia_maxima.split('(A)')
        if len(parts) > 1:
            carro.potencia_A = parts[0].strip()
            parts_G = parts[1].split('(G)')
            if len(parts_G) > 1:
                carro.potencia_G = parts_G[0].strip()
                carro.potencia_maxima = "N/D"
        else:
            carro.potencia_A = "N/D"
            carro.potencia_G = "N/D"


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
    captcha = soup.find('div', class_='g-recaptcha')

    if captcha:
        time.sleep(60)
        dr.get(url)
        response = dr.page_source
        soup = BeautifulSoup(response, 'html.parser')

    titulo_carro_element = soup.find('h1', class_='title-pousada title-bottom-border title-underblock custom')

    if titulo_carro_element:
        titulo_carro = titulo_carro_element.get_text(strip=True)
    else:
        response = dr.page_source
        soup = BeautifulSoup(response, 'html.parser')
        titulo_carro_element = soup.find('h1', class_='title-pousada title-bottom-border title-underblock custom')
        titulo_carro = titulo_carro_element.get_text(strip=True)

    # Dicionario de pares de valores
    valores = {}
    col_esq_elements = soup.find_all('div', class_='colEsq')
    for col_esq in col_esq_elements:
        chave = col_esq.get_text(strip=True)

        valor = col_esq.find_next_sibling('div', class_='colDir').get_text(strip=True)

        # Armazenando o par chave-valor no dicionario
        valores[chave] = valor

    carro = Carro(
        marca='Honda', # SEMPRE LEMBRE DE MUDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR
        modelo=titulo_carro,  # Nome do veiculo
        ano=alternative_key(valores, 'Ano:', 'Ano', 'ano'),
        combustivel=alternative_key(valores, 'Combustível:', 'Combustível', 'Combustivel:'),
        configuracao=alternative_key(valores, 'Configuração:', 'Configuração', 'Configuraçao:'),
        garantia=alternative_key(valores, 'Garantia:', 'Garantia', 'Garantia:'),
        geracao=alternative_key(valores, 'Geração:', 'Geração', 'Geraçao'),
        lugares=alternative_key(valores, 'Lugares:', 'Lugares', 'Lugar:'),
        plataforma=alternative_key(valores, 'Plataforma:', 'Plataforma', 'Plataformas:'),
        portas=alternative_key(valores, 'Portas:', 'Portas', 'Porta:'),
        porte=alternative_key(valores, 'Porte:', 'Porte', 'TEXTOALEATORIOPARANAOPEGAND'),
        procedencia=alternative_key(valores, 'Procedência:', 'Procedência', 'Procedencia:'),
        aceleracao_0_100=alternative_key(valores, 'Aceleração 0-100 km/h:', 'Aceleração 0-100 km/h', '0-100 km/h:'),
        velocidade_maxima=alternative_key(valores, 'Velocidade máxima:', 'Velocidade máxima', 'Velocidade maxima:'),
        acoplamento=alternative_key(valores, 'Acoplamento:', 'Acoplamento', 'TEXTOALEATORIOPARANAOPEGAND'),
        cambio=alternative_key(valores, 'Câmbio:', 'Câmbio', 'Cambio:'),
        codigo_cambio=alternative_key(valores, 'Código do câmbio:', 'Código do câmbio', 'Codigo do cambio:'),
        quantidade_marchas=alternative_key(valores, 'Quantidade de marchas:', 'Marchas:', 'Marcha:'),
        tracao=alternative_key(valores, 'Tração:', 'Tração', 'Tracao:'),
        alimentacao=alternative_key(valores, 'Alimentação:', 'Alimentação', 'Alimentaçao'),
        aspiracao=alternative_key(valores, 'Aspiração:', 'Aspiração', 'Aspiraçao'),
        cilindros=alternative_key(valores, 'Cilindros:', 'Cilindros', 'Cilindro'),
        codigo_motor=alternative_key(valores, 'Código do motor:', 'Código do motor', 'Código motor:'),
        comando_valvulas=alternative_key(valores, 'Comando de válvulas:', 'Comando de válvulas', 'Comando de válvula:'),
        curso_pistao=alternative_key(valores, 'Curso do pistão:', 'Curso do pistão', 'Curso dos pistões:'),
        diametro_cilindro=alternative_key(valores, 'Diâmetro do cilindro:', 'Diâmetro do cilindro',
                                          'Diâmetro dos cilindros:'),
        disposicao=alternative_key(valores, 'Disposição:', 'Disposição', 'Disposiçao:'),
        instalacao=alternative_key(valores, 'Instalação:', 'Instalação', 'Instalaçao:'),
        peso_potencia=alternative_key(valores, 'Peso/potência:', 'Peso/potência', 'Relação Peso/potência:'),
        peso_torque=alternative_key(valores, 'Peso/torque:', 'Peso/torque', 'Relação Peso/torque:'),
        potencia_especifica=alternative_key(valores, 'Potência específica:', 'Potência específica', 'Potência:'),
        potencia_G=alternative_key(valores, 'Potência máxima (G):', 'Potência (G):', 'TEXTOALEATORIOPARANAOPEGAND'),
        potencia_A=alternative_key(valores, 'Potência máxima (A):', 'Potência (A):', 'TEXTOALEATORIOPARANAOPEGAND'),
        potencia_maxima=alternative_key(valores, 'Potência máxima:', 'Potência máxima', 'TEXTOALEATORIOPARANAOPEGAND'),
        razao_compressao=alternative_key(valores, 'Razão de compressão:', 'Razão de compressão',
                                         'TEXTOALEATORIOPARANAOPEGAND'),
        torque_especifico=alternative_key(valores, 'Torque específico:', 'Torque específico', 'Torque:'),
        torque_A=alternative_key(valores, 'Torque máximo (A):', 'Torque máximo (A)', 'Torque (A):'),
        torque_G=alternative_key(valores, 'Torque máximo (G):', 'Torque máximo (G)', 'Torque (G):'),
        torque_maximo=alternative_key(valores, 'Torque máximo:', 'Torque máximo', 'TEXTOALEATORIOPARANAOPEGAND'),
        tuchos=alternative_key(valores, 'Tuchos:', 'Tuchos', 'Tucho:'),
        valvulas_por_cilindro=alternative_key(valores, 'Válvulas por cilindro:', 'Válvulas por cilindro',
                                              'Valvula por cilindro:'),
        variacao_comando=alternative_key(valores, 'Variação do comando:', 'Variação do comando',
                                         'TEXTOALEATORIOPARANAOPEGAND'),
        altura=alternative_key(valores, 'Altura:', 'Altura', 'TEXTOALEATORIOPARANAOPEGAND'),
        bitola_dianteira=alternative_key(valores, 'Bitola dianteira:', 'Bitola dianteira',
                                         'TEXTOALEATORIOPARANAOPEGAND'),
        bitola_traseira=alternative_key(valores, 'Bitola traseira:', 'Bitola traseira', 'TEXTOALEATORIOPARANAOPEGAND'),
        carga_util=alternative_key(valores, 'Carga útil:', 'Carga útil', 'TEXTOALEATORIOPARANAOPEGAND'),
        comprimento=alternative_key(valores, 'Comprimento:', 'Comprimento', 'TEXTOALEATORIOPARANAOPEGAND'),
        distancia_eixos=alternative_key(valores, 'Distância entre-eixos:', 'Distância entre-eixos',
                                        'Distância entre-eixo:'),
        largura=alternative_key(valores, 'Largura:', 'Largura', 'TEXTOALEATORIOPARANAOPEGAND'),
        peso=alternative_key(valores, 'Peso:', 'Peso', 'TEXTOALEATORIOPARANAOPEGAND'),
        porta_malas=alternative_key(valores, 'Porta-malas:', 'Porta-malas', 'Porta-mala:'),
        tanque_combustivel=alternative_key(valores, 'Tanque de combustível:', 'Tanque de combustível',
                                           'TEXTOALEATORIOPARANAOPEGAND'),
        freios_dianteiros=alternative_key(valores, 'Dianteiros:', 'Dianteiros', 'TEXTOALEATORIOPARANAOPEGAND'),
        freios_traseiros=alternative_key(valores, 'Traseiros:', 'Traseiros', 'TEXTOALEATORIOPARANAOPEGAND'),
        assistencia=alternative_key(valores, 'Assistência:', 'Assistência', 'TEXTOALEATORIOPARANAOPEGAND'),
        suspensao_dianteira=alternative_key(valores, 'Dianteira:', 'Dianteira', 'TEXTOALEATORIOPARANAOPEGAND'),
        elemento_elastico=alternative_key(valores, 'Elemento elástico:', 'Elemento elástico',
                                          'TEXTOALEATORIOPARANAOPEGAND'),
        suspensao_traseira=alternative_key(valores, 'Traseira:', 'Traseira', 'TEXTOALEATORIOPARANAOPEGAND'),
        consumo_rodoviario_G=alternative_key(valores, 'Rodoviário (G):', 'Rodoviário (G)', 'Rodoviario (G):'),
        consumo_urbano_G=alternative_key(valores, 'Urbano (G):', 'Urbano (G)', 'Urbano (G):'),
        consumo_rodoviario_A=alternative_key(valores, 'Rodoviário (A):', 'Rodoviário (A)', 'Rodoviario (A):'),
        consumo_urbano_A=alternative_key(valores, 'Urbano (A):', 'Urbano (A)', 'Urbano (A):'),
        consumo_rodoviario_D=alternative_key(valores, 'Rodoviário (D):', 'Rodoviário (D)', 'Rodoviario (D):'),
        consumo_urbano_D=alternative_key(valores, 'Urbano (D):', 'Urbano (D)', 'TEXTOALEATORIOPARANAOPEGAND'),
    )

    atualizar_campos_carro(carro)
    atualizar_campos_potencia(carro)

    lista_de_carros.append(carro)
    salvar_dados_em_csv(lista_de_carros, nome_arquivo)
    print(carro)
    print(lista_de_carros)


def main():
    urls = [
    "https://www.fichacompleta.com.br/carros/honda/civic-exs-1-8-at-2012",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxl-1-8-2012",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxl-1-8-at-2012",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-2012",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-at-2012",
    "https://www.fichacompleta.com.br/carros/honda/civic-exs-1-8-at-2013",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxl-1-8-2013",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxl-1-8-at-2013",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-2013",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-at-2013",
    "https://www.fichacompleta.com.br/carros/honda/civic-exr-2-0-2014",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxr-2-0-2014",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-2014",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-at-2014",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxr-2-0-2015",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-2015",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-at-2015",
    "https://www.fichacompleta.com.br/carros/honda/civic-exr-2-0-2016",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxr-2-0-2016",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-2016",
    "https://www.fichacompleta.com.br/carros/honda/civic-lxs-1-8-at-2016",
    "https://www.fichacompleta.com.br/carros/honda/civic-ex-2-0-at-2017",
    "https://www.fichacompleta.com.br/carros/honda/civic-exl-2-0-at-2017",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-2017",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-at-2017",
    "https://www.fichacompleta.com.br/carros/honda/civic-touring-1-5-turbo-at-2017",
    "https://www.fichacompleta.com.br/carros/honda/civic-ex-2-0-at-2018",
    "https://www.fichacompleta.com.br/carros/honda/civic-exl-2-0-at-2018",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-2018",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-at-2018",
    "https://www.fichacompleta.com.br/carros/honda/civic-touring-1-5-turbo-at-2018",
    "https://www.fichacompleta.com.br/carros/honda/civic-ex-2-0-at-2019",
    "https://www.fichacompleta.com.br/carros/honda/civic-exl-2-0-at-2019",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-2019",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-at-2019",
    "https://www.fichacompleta.com.br/carros/honda/civic-touring-1-5-turbo-at-2019",
    "https://www.fichacompleta.com.br/carros/honda/civic-ex-2-0-at-2020",
    "https://www.fichacompleta.com.br/carros/honda/civic-exl-2-0-at-2020",
    "https://www.fichacompleta.com.br/carros/honda/civic-lx-2-0-at-2020",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-at-2020",
    "https://www.fichacompleta.com.br/carros/honda/civic-touring-1-5-turbo-at-2020",
    "https://www.fichacompleta.com.br/carros/honda/civic-ex-2-0-at-2021",
    "https://www.fichacompleta.com.br/carros/honda/civic-exl-2-0-at-2021",
    "https://www.fichacompleta.com.br/carros/honda/civic-lx-2-0-at-2021",
    "https://www.fichacompleta.com.br/carros/honda/civic-sport-2-0-at-2021",
    "https://www.fichacompleta.com.br/carros/honda/civic-touring-1-5-turbo-at-2021",
    "https://www.fichacompleta.com.br/carros/honda/civic-hybrid-2-0-2023",
    "https://www.fichacompleta.com.br/carros/honda/civic-hybrid-2-0-2024"
    ]  # Link de teste!

    total_urls = len(urls)
    scrap_time = 0
    for i, url in enumerate(urls):
        print('Scraping URL {} of {}: {}'.format(i + 1, total_urls, url))
        # Perform scraping and saving to the database here (e.g., escaralhando(url))
        escaralhando(url)
        scrap_time += 1

        if scrap_time % 15 == 0 and scrap_time < total_urls:
            print("Waiting for 60 seconds...")
            time.sleep(60)  # Wait for 60 seconds every 2 scrapes
    salvar_dados_em_csv(lista_de_carros, nome_arquivo)
    print("Scraping complete for all {} URLs.".format(total_urls))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
