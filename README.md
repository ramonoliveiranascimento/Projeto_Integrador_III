# Projeto_Integrador_III
Projeto desenvolvido para a disciplina **Projeto Integrador III (PI-III)** do curso de Tecnologia em Análise e Desenvolvimento de Sistemas – FAESA.

# 🎯 ESCOPO

Este projeto visa democratizar o acesso à análise de investimentos no mercado de ações brasileiro por meio de uma plataforma web interativa. Utilizando técnicas de ciência de dados, o sistema permite comparar a performance de ativos com índices como IBOVESPA, CDI e IPCA, oferecendo visualizações acessíveis para usuários não especializados. A sociedade impactada são jovens e microinvestidores brasileiros, que frequentemente não têm acesso a ferramentas pagas ou complexas. O impacto esperado será medido por indicadores como rentabilidade simulada, uso de filtros interativos e potencial aplicação em programas de educação financeira.

```Tem como objetivo facilitar o acesso à análise de ações brasileiras por meio de uma plataforma web interativa, utilizando técnicas de ciência de dados. A proposta é gerar **insights visuais**, **simulações de rentabilidade** e **comparações com índices econômicos**, promovendo a **educação financeira** e apoiando a **tomada de decisão baseada em dados**.```

## 🧑‍🤝‍🧑 Sociedade Impactada

A plataforma tem como público-alvo:
- **Investidores iniciantes**
- **Microempreendedores e autônomos**
- **Estudantes e jovens em programas de educação financeira**
- **ONGs ou iniciativas que promovem alfabetização financeira**

O impacto social esperado é democratizar o entendimento sobre performance de ativos financeiros, contribuindo para decisões mais conscientes no mercado de capitais.

# 📌 Análise de Ações com Streamlit

Permite realizar a análise de ações de empresas listadas na bolsa brasileira (B3) utilizando a biblioteca `yfinance` para coletar dados financeiros e o `Streamlit` para construir uma interface interativa para visualização e comparação da performance dos ativos.

## 🚀 Funcionalidades

- **Gráficos interativos**: Gráfico interativo Mostrando a evolução do preço das ações no período selecionado.
- **Performance das Ações**: Exibição da performance das ações no período escolhido, com cálculos de rentabilidade.
- **Comparação com Índices Econômicos**: Comparação do desempenho das ações com o IBOVESPA, CDI e IPCA.
- **Simulação de Investimento**: Simulação de investimento inicial de R$ 1.000,00, mostrando a rentabilidade acumulada de cada ação e a carteira composta.
- **Consulta de ações brasileiras**: Com base em dados atualizados via Yahoo Finance
- **Filtros**: Por ativo e intervalo de tempo.

## 🛠 Tecnologias Utilizadas

- `Streamlit`: Para a criação da interface web interativa.
- `yfinance`: Para coleta de dados financeiros das ações.
- `pandas`: Para manipulação e análise dos dados.
- `requests` e `BeautifulSoup`: Para fazer scraping de tickers de ações da B3.
- `numpy`: Para cálculos financeiros e de rentabilidade.
- `GitHub`: Controle de versão, colaboração e entrega contínua.

## 📦 Pré-requisitos

Para rodar o projeto em sua máquina, você precisará instalar os seguintes pacotes:

*COM AMBIENTE VIRTUAL:*
    - Python 3.x
    - Pip instalado
    - Ambiente virtual (recomendado)

*SEM AMBIENTE VIRTUAL:*
    - Python 3.x
    - Pip instalado
    - Streamlit
    - yfinance
    - pandas
    - numpy
    - requests
    - BeautifulSoup

Você pode instalar as dependências com o `pip`. Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install streamlit yfinance pandas numpy requests beautifulsoup4
```

## 📥 Como Rodar o Projeto

1. Clone este repositório para sua máquina:

```bash
git clone https://github.com/ramonoliveiranascimento/NOME_DO_REPOSITORIO.git
```

2. Navegue até o diretório do projeto:

```bash
cd NOME_DO_REPOSITORIO
```
###⚠️Observação Importante ###

Crie e ative o ambiente virtual, caso opte pelo mesmo:
    ```python -m venv venv```
    
```source venv/bin/activate  # Linux/macOS```

```venv\Scripts\activate     # Windows```

3. Baixe as dependências de projetos: requirements.txt

```bash
pip install -r requirements.txt
```

4. Execute o código com o Streamlit:

```bash
streamlit run app.py
```

4. A aplicação será aberta em seu navegador padrão na URL http://localhost:8501.

## 🎨 Interface do Usuário

A interface é composta por:

**Barra Lateral:** Onde você pode selecionar as ações e o período para análise.

**Gráficos:** Exibem a evolução do preço das ações e a rentabilidade acumulada.

**Exibição de Performance:** Mostra a performance dos ativos selecionados e o desempenho total da carteira.

## ⚙ Como Funciona

*Escolha as ações:* No menu lateral, selecione uma ou mais ações para visualizar seus preços ao longo do tempo.

*Filtro de datas:* Ajuste o intervalo de datas para analisar o comportamento das ações em um período específico.

*Análise de Performance:* A aplicação calcula a rentabilidade de cada ativo selecionado e a performance da carteira com todos os ativos.

*Comparação com Índices:* Veja como as ações selecionadas se comportam em comparação com índices como o IBOVESPA, CDI e IPCA.

*Simulação de Investimento:* A aplicação simula um investimento inicial de R$ 1.000,00 e exibe o valor final de cada ativo e da carteira.

## 📈 Exemplo de Uso

Acesse a aplicação, selecione os ativos desejados, defina o período de análise e visualize:

A performance de cada ação

A evolução comparada com IBOVESPA, CDI e IPCA

Rentabilidade acumulada com investimento inicial simulado

## 🚧 Melhorias Futuras

Implementar a opção de adicionar mais índices de referência.

Incluir a opção de exportar os dados para CSV ou Excel.

Melhorar a visualização dos gráficos (por exemplo, gráficos interativos).

## 🤝 Contribuições

Sinta-se à vontade para contribuir! Se você tiver sugestões, melhorias ou correções de bugs, abra uma issue ou envie um pull request.

## 📄 Licença

Este projeto é de uso acadêmico e não se destina à recomendação financeira. Licenciado sob a MIT License.
Projeto desenvolvido para a disciplina **Projeto Integrador III (PI-III)** do curso de Tecnologia em Análise e Desenvolvimento de Sistemas – FAESA.

## 🧑‍🎓💻 DEV.

RAMON OLIVEIRA NASCIMENTO

Disciplina: Projeto Integrador III

GitHub Institucional: https://github.com/ramonoliveiranascimento
