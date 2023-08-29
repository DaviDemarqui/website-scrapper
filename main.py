import requests
from bs4 import BeautifulSoup
import mysql.connector
# imports de bibliotecas

import carro

# Configurando banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='010203',
    database='monaco'
)


def main():
    urls = ['https://www.fichacompleta.com.br/carros/volkswagen/passat-variant-2-0-tsi-2013']  # Link de teste!

    cursor = conn.cursor()

    # Estrutura do sql para salvar dados coletados...
    sql = """
        INSERT INTO ficha_carro (
            Ano, Combustivel, Configuracao, Garantia, Geração, Lugares, Plataforma, Portas,
            Porte, Procedencia, Serie, Aceleracao_0_100_km_h, Velocidade_maxima,
            Acoplamento, Cambio, Codigo_do_cambio, Quantidade_de_marchas, Tracao,
            Alimentacao, Aspiracao, Cilindrada, Cilindros, Codigo_do_motor,
            Comando_de_valvulas, Curso_do_pistao, Diametro_do_cilindro, Disposicao,
            Instalacao, Peso_potencia, Peso_torque, Potencia_especifica, Potencia_maxima,
            Razao_de_compressao, Torque_especifico, Torque_maximo, Tuchos, Valvulas_por_cilindro,
            Variacao_do_comando, Altura, Bitola_dianteira, Bitola_traseira, Carga_util,
            Comprimento, Distancia_entre_eixos, Largura, Peso, Porta_malas,
            Tanque_de_combustivel, Altura_do_flanco, Dianteiros, Estepe, Traseiros,
            Area_frontal_A, Area_frontal_corrigida, Coeficiente_de_arrasto_Cx, Assistencia,
            Diametro_minimo_de_giro, Dianteira, Elemento_elastico, Traseira,
            Rodoviaria_G, Urbana_G, Rodoviario_G, Urbano_G
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """

    for url in urls:
        print("Start scrapping page: " + url)

        # Realizando a solicitação HTTP para a pagina
        response = requests.get(url)
        print(response.status_code)
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

            dados = (
                valores['Ano:'], valores['Combustível:'], valores['Configuração:'],
                valores['Garantia:'], valores['Geração:'], valores['Lugares:'],
                valores['Plataforma:'], valores['Portas:'], valores['Porte:'],
                valores['Procedência:'], valores['Série:'], valores['Aceleração 0-100 km/h:'],
                valores['Velocidade máxima:'], valores['Acoplamento:'], valores['Câmbio:'],
                valores['Código do câmbio:'], valores['Quantidade de marchas:'],
                valores['Tração:'], valores['Alimentação:'], valores['Aspiração:'],
                valores['Cilindrada:'], valores['Cilindros:'], valores['Código do motor:'],
                valores['Comando de válvulas:'], valores['Curso do pistão:'],
                valores['Diâmetro do cilindro:'], valores['Disposição:'], valores['Instalação:'],
                valores['Peso/potência:'], valores['Peso/torque:'], valores['Potência específica:'],
                valores['Potência máxima:'], valores['Razão de compressão:'],
                valores['Torque específico:'], valores['Torque máximo:'], valores['Tuchos:'],
                valores['Válvulas por cilindro:'], valores['Variação do comando:'],
                valores['Altura:'], valores['Bitola dianteira:'], valores['Bitola traseira:'],
                valores['Carga útil:'], valores['Comprimento:'], valores['Distância entre-eixos:'],
                valores['Largura:'], valores['Peso:'], valores['Porta-malas:'],
                valores['Tanque de combustível:'], valores['Altura do flanco:'],
                valores['Dianteiros:'], valores['Estepe:'], valores['Traseiros:'],
                valores['Área frontal (A):'], valores['Área frontal corrigida:'],
                valores['Coeficiente de arrasto (Cx):'], valores['Assistência:'],
                valores['Diâmetro mínimo de giro:'], valores['Dianteira:'],
                valores['Elemento elástico:'], valores['Traseira:'], valores['Rodoviária (G):'],
                valores['Urbana (G):'], valores['Rodoviário (G):'], valores['Urbano (G):']
            )

            cursor.execute(sql, dados)
            print(dados)

            # for chave, valor in valores.items():
            #     print(f"{chave}: {valor}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
