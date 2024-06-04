# Análise de Empréstimos em Biblioteca

Este projeto faz parte do desafio #7DaysOfCode com Python Pandas.

## Descrição

Este projeto visa analisar os dados de empréstimos em uma biblioteca ao longo do tempo. Os dados incluem informações sobre os empréstimos realizados, exemplares emprestados, datas e horas dos empréstimos.

## Arquivos do Projeto

- **dados_emprestimos**: Pasta contendo arquivos CSV com dados de empréstimos separados por ano.

- **dados_exemplares.parquet**: Arquivo Parquet contendo informações sobre os exemplares da biblioteca.

- **app.py**: Script Python responsável pela importação e organização inicial dos dados.

- **analise_emprestimos.py**: Script Python para realizar a análise dos empréstimos.

- **emprestimos_completo_limpo.csv**: Arquivo CSV contendo os dados limpos após a primeira parte da análise.

## Dependências

- pandas: `pip install pandas`
- matplotlib: `pip install matplotlib`

## Execução

Para executar a análise dos empréstimos, siga estes passos:

1. Certifique-se de ter as dependências instaladas.

2. Execute o script `app.py` para importar e organizar os dados.

3. Em seguida, execute o script `analise_emprestimos.py` para realizar a análise dos empréstimos.

---

# Análise de Empréstimos em Bibliotecas Universitárias

Neste repositório, você encontrará uma série de scripts desenvolvidos para analisar os padrões de empréstimos de livros em bibliotecas universitárias ao longo do tempo. A análise é realizada com base em dados coletados entre os anos de 2010 e 2022.

## Introdução ao Boxplot

Hoje vamos discutir sobre o Boxplot, uma visualização poderosa que permite visualizar medidas estatísticas como a mediana, os quartis, os valores mínimos e máximos, e os valores atípicos (outliers). Este gráfico foi criado pelo matemático John Tukey na década de 70, no seu livro “Exploratory Data Analysis”.

O gráfico possui uma estrutura formada por uma caixa retangular, uma linha cortando essa caixa e as hastes (ou bigodes) ligadas à caixa. Os quartis são representados pelos limites da caixa, do quartil inferior (Q1) ao quartil superior (Q3). A mediana (Q2) é representada pela linha. Os valores mínimos e máximos são as extremidades das hastes e os outliers são todos os pontos além destes limites.

## Desafio do Dia

Hoje, você irá praticar algumas visualizações para entender melhor os dados e desenvolver uma análise sobre o problema dos empréstimos nas bibliotecas universitárias. Você vai:

- Identificar a coleção com maior frequência de empréstimos para cada tipo de usuário (graduação e pós-graduação).

- Plotar um gráfico de boxplot para cada ano e analisar as mudanças ao longo do tempo.

- Avaliar as diferenças nos empréstimos entre os alunos de graduação e pós-graduação e identificar anos específicos que se destacam.

- Realizar análises comparativas entre diferentes anos para entender as tendências nos empréstimos.

Além disso, você vai realizar uma análise detalhada dos empréstimos realizados pelos cursos de graduação entre 2015 e 2020, e calcular a quantidade de empréstimos por ano para cada curso.

Por fim, você irá comparar a diferença percentual nos empréstimos entre os anos de 2017-2018, 2018-2019 e 2019-2022, destacando as mudanças ao longo do tempo.

## Estrutura do Projeto

- `analise_emprestimos_pos_graduacao.py`: Script principal que contém as análises e visualizações dos empréstimos.

- `data/`: Pasta contendo os dados de empréstimos em diferentes formatos (CSV, Excel, JSON).

- `resultados/`: Pasta onde são salvos os resultados das análises (gráficos, tabelas).

## Como Executar

Para executar o script principal, basta rodar o comando `python analise_emprestimos_pos_graduacao.py` no terminal.

## Bibliotecas Utilizadas

- Pandas
- Matplotlib
- Seaborn

