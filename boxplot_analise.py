import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

# Carregar os dados
emprestimos_completo = pd.read_csv('emprestimos_completo_limpo.csv')

# Verificar os dados carregados
print(emprestimos_completo.head())

# Filtrar dados para alunos de graduação
alunos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE GRADUAÇÃO"')
print(alunos_graduacao['colecao'].value_counts())

# Cria a tabela de frequência mensal por ano para alunos de graduação na coleção Acervo Circulante
alunos_graduacao_acervo_circulante = alunos_graduacao.query('colecao == "Acervo Circulante"')
alunos_graduacao_acervo_circulante = pd.DataFrame(alunos_graduacao_acervo_circulante)
alunos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_graduacao_acervo_circulante['data_emprestimo'])
alunos_graduacao_acervo_circulante['ano'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.year
alunos_graduacao_acervo_circulante['mes'] = alunos_graduacao_acervo_circulante['data_emprestimo'].dt.month
alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.loc[:, ['ano', 'mes']]
alunos_graduacao_acervo_circulante = alunos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()
print(alunos_graduacao_acervo_circulante)

# Função para gerar boxplot
def gera_box_plot(dataset, x, y, titulo, subtitulo, filename):
    sns.set_theme(style="darkgrid", palette='Blues', font_scale=1.3)
    plt.figure(figsize=(16, 10))
    ax = sns.boxplot(x=x, y=y, data=dataset, color='#4171EF')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',', '.')))
    plt.ylim(0, max(dataset[y]) * 1.1)
    plt.xlabel(None)
    plt.ylabel(None)
    ax.set_title(titulo + "\n", size=20, loc='left', weight='bold')
    ax.text(s=subtitulo, x=-0.5, y=max(dataset[y]) * 1.11, fontsize=18, ha='left', color='gray')
    plt.savefig(filename)
    plt.close()

# Distribuição dos empréstimos mensais realizados pelos alunos de graduação na coleção do acervo circulante
gera_box_plot(alunos_graduacao_acervo_circulante, 'ano', 'quantidade', 'Distribuição dos empréstimos mensais', 'Realizados pelos alunos de graduação no acervo circulante', 'boxplot_graduacao.png')

# Filtra os dados para alunos de pós-graduação
alunos_pos_graduacao = emprestimos_completo.query('tipo_vinculo_usuario == "ALUNO DE PÓS-GRADUAÇÃO"')
print(alunos_pos_graduacao['colecao'].value_counts())

# Criar a tabela de frequência mensal por ano para alunos de pós-graduação na coleção Acervo Circulante
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao.query('colecao == "Acervo Circulante"')
alunos_pos_graduacao_acervo_circulante = pd.DataFrame(alunos_pos_graduacao_acervo_circulante)
alunos_pos_graduacao_acervo_circulante['data_emprestimo'] = pd.to_datetime(alunos_pos_graduacao_acervo_circulante['data_emprestimo'])
alunos_pos_graduacao_acervo_circulante['ano'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.year
alunos_pos_graduacao_acervo_circulante['mes'] = alunos_pos_graduacao_acervo_circulante['data_emprestimo'].dt.month
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.loc[:, ['ano', 'mes']]
alunos_pos_graduacao_acervo_circulante = alunos_pos_graduacao_acervo_circulante.value_counts().to_frame('quantidade').reset_index()
print(alunos_pos_graduacao_acervo_circulante)

# Distribuição dos empréstimos mensais realizados pelos alunos de pós-graduação na coleção do acervo circulante
gera_box_plot(alunos_pos_graduacao_acervo_circulante, 'ano', 'quantidade', 'Distribuição dos empréstimos mensais', 'Realizados pelos alunos de pós-graduação no acervo circulante', 'boxplot_pos_graduacao.png')

print("Gráficos de boxplot gerados e salvos como 'boxplot_graduacao.png' e 'boxplot_pos_graduacao.png'.")
