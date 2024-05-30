import pandas as pd

def gerar_tabela_frequencia(df, coluna):
    """
    Gera uma tabela de frequência e percentual para uma variável categórica.

    Parâmetros:
    df (DataFrame): O DataFrame contendo os dados.
    coluna (str): O nome da coluna para a qual gerar a tabela.

    Retorna:
    DataFrame: Tabela de frequência e percentual.
    """
    try:
        frequencia = df[coluna].value_counts()
        percentual = df[coluna].value_counts(normalize=True) * 100
        tabela = pd.DataFrame({'Frequência': frequencia, 'Percentual (%)': percentual.round(2)})
        return tabela
    except KeyError:
        print(f"Erro: A coluna '{coluna}' não existe no DataFrame.")
        return None

# Leitura dos dados limpos
emprestimos_completo = pd.read_csv('emprestimos_completo_limpo.csv')

# Exibir as colunas do DataFrame
print("Colunas do DataFrame:")
print(emprestimos_completo.columns)

# Gerar tabelas de frequência e percentual para as variáveis categóricas
colunas_categoricas = ['tipo_vinculo_usuario', 'colecao', 'biblioteca', 'classe_cdu']
tabelas = {}

for coluna in colunas_categoricas:
    tabela = gerar_tabela_frequencia(emprestimos_completo, coluna)
    if tabela is not None:
        tabelas[coluna] = tabela

# Exibir tabelas
for coluna, tabela in tabelas.items():
    print(f"\nDistribuição dos Empréstimos por {coluna.replace('_', ' ').title()}:")
    print(tabela)
