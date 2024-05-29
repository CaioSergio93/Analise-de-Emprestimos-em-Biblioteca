import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados limpos
emprestimos_completo = pd.read_csv('emprestimos_completo_limpo.csv')

# Verificar as colunas presentes no DataFrame
print("Colunas disponíveis no DataFrame:", emprestimos_completo.columns)

# Convertendo as colunas de datas e horas para o tipo datetime
emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo['data_emprestimo'])

# Verificar se a coluna 'hora_emprestimo' está presente
if 'hora_emprestimo' in emprestimos_completo.columns:
    emprestimos_completo['hora_emprestimo'] = pd.to_datetime(emprestimos_completo['hora_emprestimo']).dt.hour

    # 3. Horários com maior quantidade de empréstimos ao longo de um dia
    emprestimos_por_hora = emprestimos_completo.groupby('hora_emprestimo')['id_exemplar'].count()

    # Plotando um gráfico de barras para os horários com maior quantidade de empréstimos
    plt.figure(figsize=(10, 6))
    emprestimos_por_hora.plot(kind='bar', color='r')
    plt.title('Quantidade de Exemplares Emprestados por Hora do Dia')
    plt.xlabel('Hora do Dia')
    plt.ylabel('Quantidade de Exemplares')
    plt.grid(True)
    plt.show()
else:
    print("A coluna 'hora_emprestimo' não está presente no DataFrame. Pulando a análise por hora.")

# 1. Quantidade total de exemplares emprestados por ano
emprestimos_por_ano = emprestimos_completo.groupby(emprestimos_completo['data_emprestimo'].dt.year)['id_exemplar'].count()

# Plotando um gráfico de linhas para a quantidade total de exemplares emprestados por ano
plt.figure(figsize=(10, 6))
emprestimos_por_ano.plot(marker='o', color='b')
plt.title('Quantidade Total de Exemplares Emprestados por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Exemplares')
plt.grid(True)
plt.show()

# 2. Quantidade total de exemplares emprestados por mês
emprestimos_completo['ano_mes'] = emprestimos_completo['data_emprestimo'].dt.to_period('M')
emprestimos_por_mes = emprestimos_completo.groupby('ano_mes')['id_exemplar'].count()

# Plotando um gráfico de linhas para a quantidade total de exemplares emprestados por mês
plt.figure(figsize=(10, 6))
emprestimos_por_mes.plot(marker='o', color='g')
plt.title('Quantidade Total de Exemplares Emprestados por Mês')
plt.xlabel('Mês e Ano')
plt.ylabel('Quantidade de Exemplares')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
