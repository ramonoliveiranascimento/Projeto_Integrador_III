import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import numpy as np
import requests
from bs4 import BeautifulSoup

# Configuração da página
st.set_page_config(page_title="Análise de Ações", layout="wide")

# Datas padrão
DATA_INICIO = "2000-01-01"
DATA_ATUAL = datetime.datetime.today().strftime('%Y-%m-%d')

# Função para carregar dados das ações
@st.cache_data
def carregar_dados(empresas):
    formato_texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(formato_texto_tickers)
    cotacoes_acao = dados_acao.history(start=DATA_INICIO, end=DATA_ATUAL)
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

@st.cache_data
def carrega_ticker_acoes():
  # URL da página
  url = "https://www.dadosdemercado.com.br/acoes"

  # Fazer a requisição GET para acessar a página
  response = requests.get(url, timeout=10)

  # Verificar se a requisição foi bem sucedida
  if response.status_code == 200:
      print("Página acessada com sucesso!")
      
      # Analisar o conteúdo HTML com BeautifulSoup
      soup = BeautifulSoup(response.text, 'html.parser')
      
      # Encontrar a tabela com os dados
      tabela = soup.find('table', {'class': 'normal-table'})  # A classe pode variar, então verifique no HTML

      # Extrair os dados da tabela para um DataFrame
      tabela_linhas = tabela.find_all('tr')

      # Extrair os títulos das colunas
      colunas = [th.text.strip() for th in tabela_linhas[0].find_all('th')]

      # Extrair os dados das linhas
      dados = []
      for linha in tabela_linhas[1:]:  # Começa a partir da segunda linha, pois a primeira é o cabeçalho
          colunas_linhas = linha.find_all('td')
          if len(colunas_linhas) > 1:  # Ignorar linhas vazias
              dados.append([coluna.text.strip() for coluna in colunas_linhas])

      # Criar um DataFrame
      df = pd.DataFrame(dados, columns=colunas)

      # Coloca a palavra .SA nas ações
      base_tickers = pd.DataFrame(df)
      tickers = list(base_tickers["Ticker"])
      tickers = [item + ".SA" for item in tickers]
      
      return tickers
  
  else:
      print("Erro ao acessar a página!")

# Comparação com índices econômicos
@st.cache_data
def carregar_indices():

    ibovespa = yf.Ticker("^BVSP").history(start=DATA_INICIO, end=DATA_ATUAL)["Close"]

    # Simulando CDI e IPCA com crescimento composto diário
    cdi_ao_ano = 0.13
    ipca_ao_ano = 0.05
    dias_ano = 252

    cdi_diario = (1 + cdi_ao_ano) ** (1 / dias_ano) - 1
    ipca_diario = (1 + ipca_ao_ano) ** (1 / dias_ano) - 1

    cdi_acumulado = (1 + cdi_diario) ** np.arange(len(ibovespa)) - 1
    ipca_acumulado = (1 + ipca_diario) ** np.arange(len(ibovespa)) - 1

    indices_df = pd.DataFrame({
        "IBOVESPA": ibovespa,
        "CDI": pd.Series(cdi_acumulado, index=ibovespa.index),
        "IPCA": pd.Series(ipca_acumulado, index=ibovespa.index)
    })

    return indices_df

acoes = carrega_ticker_acoes()
dados = carregar_dados(acoes)

# Barra lateral - Filtros
st.sidebar.header("Filtros")

# Filtro ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar:", dados.columns)

if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})
else:
    dados = pd.DataFrame()  # Gera um DataFrame vazio

# Filtro datas
# Melhorias para evitar erro no filtro de datas
if not dados.empty:
    data_inicial = dados.index.min().to_pydatetime()
    data_final = dados.index.max().to_pydatetime()

    intervalo_data = st.sidebar.slider(
        "Selecione o período:",
        min_value=data_inicial,
        max_value=data_final,
        value=(data_inicial, data_final)
    )

    dados = dados[(dados.index >= intervalo_data[0]) & (dados.index <= intervalo_data[1])]


# Interface do Streamlit
if not dados.empty:
    st.write("""
             # 📈 PREÇO DE AÇÕES
             O gráfico abaixo apresenta a evolução do preço das ações ao longo do tempo.
             """)

    # Gráfico
    st.line_chart(dados)

    # Performance dos ativos
    texto_performance_ativos = ""

    if len(lista_acoes) == 1:
        dados = dados.rename(columns={"Close": acao_unica})

    # Cálculo da performance
    carteira = [1000 for acao in lista_acoes]
    total_inicial_carteira = sum(carteira)

    for i, acao in enumerate(lista_acoes):
        performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
        performance_ativo = float(performance_ativo)

        if np.isnan(performance_ativo):
            texto_performance_ativos_nao_encontrado = "PARA ESTE ATIVO: Informe um período maior ou igual à sua data de início!"
            texto_performance_ativos = texto_performance_ativos + f"  \n{acao}: :orange[{texto_performance_ativos_nao_encontrado}]"
        else:
            carteira[i] = carteira[i] * (1 + performance_ativo)
            if performance_ativo > 0:
                texto_performance_ativos += f"  \n{acao}: :green[{performance_ativo:.1%}]"
            elif performance_ativo < 0:
                texto_performance_ativos += f"  \n{acao}: :red[{performance_ativo:.1%}]"
            else:
                texto_performance_ativos += f"  \n{acao}: {performance_ativo:.1%}"

    total_final_carteira = sum(carteira)
    performance_carteira = total_final_carteira / total_inicial_carteira - 1

    if performance_carteira > 0:
        texto_performance_carteira = f"Performance da carteira com todos os ativos:  :green[{performance_carteira:.1%}]"
    elif performance_carteira < 0:
        texto_performance_carteira = f"Performance da carteira com todos os ativos:  :red[{performance_carteira:.1%}]"
    else:
        texto_performance_carteira = f"Performance da carteira com todos os ativos: {performance_carteira:.1%}"

    st.write(f"""### 📈 PERFORMANCE DOS ATIVOS""")
    st.write(f"""Essa foi a performance dos ativos no período selecionado:{texto_performance_ativos}""")
    st.write(f"""{texto_performance_carteira}""")
    
    # Comparação com índices econômicos
    indices = carregar_indices()
    intervalo_data = [data.replace(tzinfo=None) for data in intervalo_data]
    indices.index = indices.index.tz_localize(None)
    indices = indices.loc[intervalo_data[0]:intervalo_data[1]]

    # Simulação de investimento inicial
    investimento_inicial = 1000
    indices_rentabilidade = (indices / indices.iloc[0]) * investimento_inicial
    carteira_rentabilidade = (dados / dados.iloc[0]) * investimento_inicial

    comparacao_df = indices_rentabilidade.copy()
    comparacao_df["Carteira"] = carteira_rentabilidade.sum(axis=1) / len(lista_acoes)

    # Plotando o gráfico de rentabilidade ao longo do tempo
    st.write("### Comparação de Rentabilidade Acumulada")
    st.line_chart(comparacao_df)

    # Exibição dos valores finais
    st.write("### Simulação de Investimento Inicial: R$ 1.000,00")
    for indice in indices.columns:
        st.write(f"{indice}: R$ {indices_rentabilidade[indice].iloc[-1]:,.2f}")
    for acao in lista_acoes:
        st.write(f"{acao}: R$ {carteira_rentabilidade[acao].iloc[-1]:,.2f}")
    st.write(f"Carteira Total: R$ {comparacao_df['Carteira'].iloc[-1]:,.2f}")

else:
    st.write("Selecione um ou mais ativos!")