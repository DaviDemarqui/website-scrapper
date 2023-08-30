import random
import time

import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# imports de bibliotecas

# Configurações principais!
Base = declarative_base()


# Configurando modelo carro
class Carro(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True)
    titulo_carro = Column(String(255))
    ano = Column(String(255))
    combustivel = Column(String(255))
    configuracao = Column(String(255))
    garantia = Column(String(255))
    geracao = Column(String(255))
    lugares = Column(String(255))
    plataforma = Column(String(255))
    portas = Column(String(255))
    porte = Column(String(255))
    procedencia = Column(String(255))
    serie = Column(String(255))
    aceleracao_0_100 = Column(String(255))
    velocidade_maxima = Column(String(255))
    acoplamento = Column(String(255))
    cambio = Column(String(255))
    codigo_cambio = Column(String(255))
    quantidade_marchas = Column(String(255))
    tracao = Column(String(255))
    alimentacao = Column(String(255))
    aspiracao = Column(String(255))
    cilindrada = Column(String(255))
    cilindros = Column(String(255))
    codigo_motor = Column(String(255))
    comando_valvulas = Column(String(255))
    curso_pistao = Column(String(255))
    diametro_cilindro = Column(String(255))
    disposicao = Column(String(255))
    instalacao = Column(String(255))
    peso_potencia = Column(String(255))
    peso_torque = Column(String(255))
    potencia_especifica = Column(String(255))
    potencia_maxima = Column(String(255))
    razao_compressao = Column(String(255))
    torque_especifico = Column(String(255))
    torque_maximo = Column(String(255))
    tuchos = Column(String(255))
    valvulas_por_cilindro = Column(String(255))
    variacao_comando = Column(String(255))
    altura = Column(String(255))
    bitola_dianteira = Column(String(255))
    bitola_traseira = Column(String(255))
    carga_util = Column(String(255))
    comprimento = Column(String(255))
    distancia_eixos = Column(String(255))
    largura = Column(String(255))
    peso = Column(String(255))
    porta_malas = Column(String(255))
    tanque_combustivel = Column(String(255))
    altura_flanco = Column(String(255))
    dianteiros = Column(String(255))
    estepe = Column(String(255))
    traseiros = Column(String(255))
    area_frontal_a = Column(String(255))
    area_frontal_corrigida = Column(String(255))
    coeficiente_arrasto_cx = Column(String(255))
    assistencia = Column(String(255))
    diametro_giro = Column(String(255))
    dianteira = Column(String(255))
    elemento_elastico = Column(String(255))
    traseira = Column(String(255))
    rodoviaria_g = Column(String(255))
    urbana_g = Column(String(255))
    rodoviario_g = Column(String(255))
    urbano_g = Column(String(255))



mysql_url = 'mysql://root:010203@localhost/monaco'

engine = create_engine(mysql_url)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


#  Busca por keywork alternativo
def alternative_key(dictionary, key, alternate_key, default='Sem Informação'):
    try:
        return dictionary[key]
    except KeyError:
        try:
            return dictionary[alternate_key]
        except KeyError:
            return default


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
    response = requests.get(url, headers)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrando todos os elementos com a classe "colEsq"
        # Geralmente são titulos como ex: Marca, Combustivel etc...
        col_esq_elements = soup.find_all('div', class_='colEsq')
        titulo_carro = soup.find('h1', class_='title-pousada title-bottom-border title-underblock custom').get_text(
            strip=True)

        # Dicionario de pares de valores
        valores = {}

        for col_esq in col_esq_elements:
            chave = col_esq.get_text(strip=True)

            valor = col_esq.find_next_sibling('div', class_='colDir').get_text(strip=True)

            # Armazenando o par chave-valor no dicionario
            valores[chave] = valor

        # dados = (
        #     1,
        #     titulo_carro,  # Nome do veiculo
        #     alternative_key(valores, 'Ano:', 'Ano'),
        #     alternative_key(valores, 'Combustível:', 'Combustível'),
        #     alternative_key(valores, 'Configuração:', 'Configuração'),
        #     alternative_key(valores, 'Garantia:', 'Garantia'),
        #     alternative_key(valores, 'Geração:', 'Geração'),
        #     alternative_key(valores, 'Lugares:', 'Lugares'),
        #     alternative_key(valores, 'Plataforma:', 'Plataforma'),
        #     alternative_key(valores, 'Portas:', 'Portas'),
        #     alternative_key(valores, 'Porte:', 'Porte'),
        #     alternative_key(valores, 'Procedência:', 'Procedência'),
        #     alternative_key(valores, 'Série:', 'Série'),
        #     alternative_key(valores, 'Aceleração 0-100 km/h:', 'Aceleração 0-100 km/h'),
        #     alternative_key(valores, 'Velocidade máxima:', 'Velocidade máxima'),
        #     alternative_key(valores, 'Acoplamento:', 'Acoplamento'),
        #     alternative_key(valores, 'Câmbio:', 'Câmbio'),
        #     alternative_key(valores, 'Código do câmbio:', 'Código do câmbio'),
        #     alternative_key(valores, 'Quantidade de marchas:', 'Marchas'),
        #     alternative_key(valores, 'Tração:', 'Tração'),
        #     alternative_key(valores, 'Alimentação:', 'Alimentação'),
        #     alternative_key(valores, 'Aspiração:', 'Aspiração'),
        #     alternative_key(valores, 'Cilindrada:', 'Cilindrada'),
        #     alternative_key(valores, 'Cilindros:', 'Cilindros'),
        #     alternative_key(valores, 'Código do motor:', 'Código do motor'),
        #     alternative_key(valores, 'Comando de válvulas:', 'Comando de válvulas'),
        #     alternative_key(valores, 'Curso do pistão:', 'Curso do pistão'),
        #     alternative_key(valores, 'Diâmetro do cilindro:', 'Diâmetro do cilindro'),
        #     alternative_key(valores, 'Disposição:', 'Disposição'),
        #     alternative_key(valores, 'Instalação:', 'Instalação'),
        #     alternative_key(valores, 'Peso/potência:', 'Peso/potência'),
        #     alternative_key(valores, 'Peso/torque:', 'Peso/torque'),
        #     alternative_key(valores, 'Potência específica:', 'Potência específica'),
        #     alternative_key(valores, 'Potência máxima:', 'Potência máxima'),
        #     alternative_key(valores, 'Razão de compressão:', 'Razão de compressão'),
        #     alternative_key(valores, 'Torque específico:', 'Torque específico'),
        #     alternative_key(valores, 'Torque máximo:', 'Torque máximo'),
        #     alternative_key(valores, 'Tuchos:', 'Tuchos'),
        #     alternative_key(valores, 'Válvulas por cilindro:', 'Válvulas por cilindro'),
        #     alternative_key(valores, 'Variação do comando:', 'Variação do comando'),
        #     alternative_key(valores, 'Altura:', 'Altura'),
        #     alternative_key(valores, 'Bitola dianteira:', 'Bitola dianteira'),
        #     alternative_key(valores, 'Bitola traseira:', 'Bitola traseira'),
        #     alternative_key(valores, 'Carga útil:', 'Carga útil'),
        #     alternative_key(valores, 'Comprimento:', 'Comprimento'),
        #     alternative_key(valores, 'Distância entre-eixos:', 'Distância entre-eixos'),
        #     alternative_key(valores, 'Largura:', 'Largura'),
        #     alternative_key(valores, 'Peso:', 'Peso'),
        #     alternative_key(valores, 'Porta-malas:', 'Porta-malas'),
        #     alternative_key(valores, 'Tanque de combustível:', 'Tanque de combustível'),
        #     alternative_key(valores, 'Altura do flanco:', 'Altura do flanco'),
        #     alternative_key(valores, 'Dianteiros:', 'Dianteiros'),
        #     alternative_key(valores, 'Estepe:', 'Estepe'),
        #     alternative_key(valores, 'Traseiros:', 'Traseiros'),
        #     alternative_key(valores, 'Área frontal (A):', 'Área frontal (A)'),
        #     alternative_key(valores, 'Área frontal corrigida:', 'Área frontal corrigida'),
        #     alternative_key(valores, 'Coeficiente de arrasto (Cx):', 'Coeficiente de arrasto (Cx)'),
        #     alternative_key(valores, 'Assistência:', 'Assistência'),
        #     alternative_key(valores, 'Diâmetro mínimo de giro:', 'Diâmetro mínimo de giro'),
        #     alternative_key(valores, 'Dianteira:', 'Dianteira'),
        #     alternative_key(valores, 'Elemento elástico:', 'Elemento elástico'),
        #     alternative_key(valores, 'Traseira:', 'Traseira'),
        #     alternative_key(valores, 'Rodoviária (G):', 'Rodoviária (G)'),
        #     alternative_key(valores, 'Urbana (G):', 'Urbana (G)'),
        #     alternative_key(valores, 'Rodoviário (G):', 'Rodoviário (G)'),
        #     alternative_key(valores, 'Urbano (G):', 'Urbano (G)')
        # )
        carro = Carro(
            titulo_carro=titulo_carro,  # Nome do veiculo
            ano=alternative_key(valores, 'Ano:', 'Ano'),
            combustivel=alternative_key(valores, 'Combustível:', 'Combustível'),
            configuracao=alternative_key(valores, 'Configuração:', 'Configuração'),
            garantia=alternative_key(valores, 'Garantia:', 'Garantia'),
            geracao=alternative_key(valores, 'Geração:', 'Geração'),
            lugares=alternative_key(valores, 'Lugares:', 'Lugares'),
            plataforma=alternative_key(valores, 'Plataforma:', 'Plataforma'),
            portas=alternative_key(valores, 'Portas:', 'Portas'),
            porte=alternative_key(valores, 'Porte:', 'Porte'),
            procedencia=alternative_key(valores, 'Procedência:', 'Procedência'),
            serie=alternative_key(valores, 'Série:', 'Série'),
            aceleracao_0_100=alternative_key(valores, 'Aceleração 0-100 km/h:', 'Aceleração 0-100 km/h'),
            velocidade_maxima=alternative_key(valores, 'Velocidade máxima:', 'Velocidade máxima'),
            acoplamento=alternative_key(valores, 'Acoplamento:', 'Acoplamento'),
            cambio=alternative_key(valores, 'Câmbio:', 'Câmbio'),
            codigo_cambio=alternative_key(valores, 'Código do câmbio:', 'Código do câmbio'),
            quantidade_marchas=alternative_key(valores, 'Quantidade de marchas:', 'Marchas'),
            tracao=alternative_key(valores, 'Tração:', 'Tração'),
            alimentacao=alternative_key(valores, 'Alimentação:', 'Alimentação'),
            aspiracao=alternative_key(valores, 'Aspiração:', 'Aspiração'),
            cilindrada=alternative_key(valores, 'Cilindrada:', 'Cilindrada'),
            cilindros=alternative_key(valores, 'Cilindros:', 'Cilindros'),
            codigo_motor=alternative_key(valores, 'Código do motor:', 'Código do motor'),
            comando_valvulas=alternative_key(valores, 'Comando de válvulas:', 'Comando de válvulas'),
            curso_pistao=alternative_key(valores, 'Curso do pistão:', 'Curso do pistão'),
            diametro_cilindro=alternative_key(valores, 'Diâmetro do cilindro:', 'Diâmetro do cilindro'),
            disposicao=alternative_key(valores, 'Disposição:', 'Disposição'),
            instalacao=alternative_key(valores, 'Instalação:', 'Instalação'),
            peso_potencia=alternative_key(valores, 'Peso/potência:', 'Peso/potência'),
            peso_torque=alternative_key(valores, 'Peso/torque:', 'Peso/torque'),
            potencia_especifica=alternative_key(valores, 'Potência específica:', 'Potência específica'),
            potencia_maxima=alternative_key(valores, 'Potência máxima:', 'Potência máxima'),
            razao_compressao=alternative_key(valores, 'Razão de compressão:', 'Razão de compressão'),
            torque_especifico=alternative_key(valores, 'Torque específico:', 'Torque específico'),
            torque_maximo=alternative_key(valores, 'Torque máximo:', 'Torque máximo'),
            tuchos=alternative_key(valores, 'Tuchos:', 'Tuchos'),
            valvulas_por_cilindro=alternative_key(valores, 'Válvulas por cilindro:', 'Válvulas por cilindro'),
            variacao_comando=alternative_key(valores, 'Variação do comando:', 'Variação do comando'),
            altura=alternative_key(valores, 'Altura:', 'Altura'),
            bitola_dianteira=alternative_key(valores, 'Bitola dianteira:', 'Bitola dianteira'),
            bitola_traseira=alternative_key(valores, 'Bitola traseira:', 'Bitola traseira'),
            carga_util=alternative_key(valores, 'Carga útil:', 'Carga útil'),
            comprimento=alternative_key(valores, 'Comprimento:', 'Comprimento'),
            distancia_eixos=alternative_key(valores, 'Distância entre-eixos:', 'Distância entre-eixos'),
            largura=alternative_key(valores, 'Largura:', 'Largura'),
            peso=alternative_key(valores, 'Peso:', 'Peso'),
            porta_malas=alternative_key(valores, 'Porta-malas:', 'Porta-malas'),
            tanque_combustivel=alternative_key(valores, 'Tanque de combustível:', 'Tanque de combustível'),
            altura_flanco=alternative_key(valores, 'Altura do flanco:', 'Altura do flanco'),
            dianteiros=alternative_key(valores, 'Dianteiros:', 'Dianteiros'),
            estepe=alternative_key(valores, 'Estepe:', 'Estepe'),
            traseiros=alternative_key(valores, 'Traseiros:', 'Traseiros'),
            area_frontal_a=alternative_key(valores, 'Área frontal (A):', 'Área frontal (A)'),
            area_frontal_corrigida=alternative_key(valores, 'Área frontal corrigida:', 'Área frontal corrigida'),
            coeficiente_arrasto_cx=alternative_key(valores, 'Coeficiente de arrasto (Cx):',
                                                   'Coeficiente de arrasto (Cx)'),
            assistencia=alternative_key(valores, 'Assistência:', 'Assistência'),
            diametro_giro=alternative_key(valores, 'Diâmetro mínimo de giro:', 'Diâmetro mínimo de giro'),
            dianteira=alternative_key(valores, 'Dianteira:', 'Dianteira'),
            elemento_elastico=alternative_key(valores, 'Elemento elástico:', 'Elemento elástico'),
            traseira=alternative_key(valores, 'Traseira:', 'Traseira'),
            rodoviaria_g=alternative_key(valores, 'Rodoviária (G):', 'Rodoviária (G)'),
            urbana_g=alternative_key(valores, 'Urbana (G):', 'Urbana (G)'),
            rodoviario_g=alternative_key(valores, 'Rodoviário (G):', 'Rodoviário (G)'),
            urbano_g=alternative_key(valores, 'Urbano (G):', 'Urbano (G)')
        )

        session.add(carro)
        session.commit()
        session.close()


def main():
    urls = ['https://www.fichacompleta.com.br/carros/volkswagen/passat-variant-3-2-v6-fsi-2007',
            'https://www.fichacompleta.com.br/carros/volkswagen/passat-variant-3-2-v6-fsi-2010',
            'https://www.fichacompleta.com.br/carros/volkswagen/passat-variant-2-0-tsi-2013']  # Link de teste!

    scrap_time = 0
    for url in urls:
        print('Scrapping number: ', scrap_time)
        # Usando if para configurar o timer!
        if scrap_time <= 1:
            escaralhando(url)  # Essa função vai realizar o scraping e salvar no banco!
            scrap_time = 5
        else:
            print("")
            time.sleep(60)  # Timer para realizar o scrapping apos 60 segundos :)
            escaralhando(url)

    # for chave, valor in valores.items():
    #     print(f"{chave}: {valor}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
