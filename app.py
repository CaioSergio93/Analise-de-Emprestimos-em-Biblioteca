import pandas as pd

# Caminho para a pasta com os arquivos CSV
caminho_base = 'C:/Users/caios/Documents/Ciencia de Dados/7DaysOfCode/Code/dados_emprestimos'

# Leitura dos dados de empréstimos
dados_2010_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20101.csv')
dados_2010_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20102.csv')
dados_2011_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20111.csv')
dados_2011_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20112.csv')
dados_2012_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20121.csv')
dados_2012_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20122.csv')
dados_2013_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20131.csv')
dados_2013_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20132.csv')
dados_2014_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20141.csv')
dados_2014_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20142.csv')
dados_2015_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20151.csv')
dados_2015_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20152.csv')
dados_2016_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20161.csv')
dados_2016_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20162.csv')
dados_2017_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20171.csv')
dados_2017_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20172.csv')
dados_2018_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20181.csv')
dados_2018_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20182.csv')
dados_2019_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20191.csv')
dados_2019_2 = pd.read_csv(f'{caminho_base}\\emprestimos-20192.csv')
dados_2020_1 = pd.read_csv(f'{caminho_base}\\emprestimos-20201.csv')

# Combinação dos dados
emprestimos_biblioteca = pd.concat([dados_2010_1, dados_2010_2, dados_2011_1, dados_2011_2, dados_2012_1, dados_2012_2,
                                    dados_2013_1, dados_2013_2, dados_2014_1, dados_2014_2, dados_2015_1, dados_2015_2,
                                    dados_2016_1, dados_2016_2, dados_2017_1, dados_2017_2, dados_2018_1, dados_2018_2,
                                    dados_2019_1, dados_2019_2, dados_2020_1], ignore_index=True)

# Remoção de duplicatas
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()

# Exibição das primeiras linhas
print(emprestimos_biblioteca.head())

# Leitura dos dados dos exemplares
caminho_exemplares = 'C:/Users/caios/Documents/Ciencia de Dados/7DaysOfCode/Code/dados_exemplares.parquet'
dados_exemplares = pd.read_parquet(caminho_exemplares)
print(dados_exemplares.head())

# Combinação dos dados de empréstimos e exemplares
emprestimos_completo = emprestimos_biblioteca.merge(dados_exemplares)
print(emprestimos_completo.head())

# Função para mapear os valores da localização para as classes gerais da CDU
def mapear_classe_cdu(localizacao):
    classe = int(localizacao) // 100
    if classe >= 0 and classe <= 99:
        return 'Generalidades. Ciência e conhecimento'
    elif classe >= 100 and classe <= 199:
        return 'Filosofia e psicologia'
    elif classe >= 200 and classe <= 299:
        return 'Religião'
    elif classe >= 300 and classe <= 399:
        return 'Ciências sociais'
    elif classe >= 400 and classe <= 499:
        return 'Classe vaga. Provisoriamente não ocupada'
    elif classe >= 500 and classe <= 599:
        return 'Matemática e ciências naturais'
    elif classe >= 600 and classe <= 699:
        return 'Ciências aplicadas'
    elif classe >= 700 and classe <= 799:
        return 'Belas artes'
    elif classe >= 800 and classe <= 899:
        return 'Linguagem. Língua. Linguística'
    elif classe >= 900 and classe <= 999:
        return 'Geografia. Biografia. História'
    else:
        return 'Classe inválida'

# Criar uma nova coluna com as classes gerais da CDU
emprestimos_completo['classe_cdu'] = emprestimos_completo['localizacao'].apply(mapear_classe_cdu)

# Excluir a coluna "registro_sistema"
emprestimos_completo.drop(columns=['registro_sistema'], inplace=True)

# Modificar a coluna "matricula_ou_siape" para o formato String
emprestimos_completo['matricula_ou_siape'] = emprestimos_completo['matricula_ou_siape'].astype(str)

# Salvar os dados limpos em um novo arquivo CSV
emprestimos_completo.to_csv('emprestimos_completo_limpo.csv', index=False)

# Exibir as primeiras linhas dos dados limpos
print(emprestimos_completo.head())
