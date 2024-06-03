import pandas as pd

# Leitura dos dados do Excel
try:
    cadastro_usuarios_antes_2010 = pd.read_excel('matricula_alunos.xlsx', sheet_name='Até 2010', skiprows=1)
    cadastro_usuarios_depois_2010 = pd.read_excel('matricula_alunos.xlsx', sheet_name='Após 2010', skiprows=1)
except FileNotFoundError:
    print("Erro: Arquivo 'matricula_alunos.xlsx' não encontrado.")
    exit()

# Renomeando colunas
cadastro_usuarios_antes_2010.columns = ['matricula_ou_siape', 'tipo_vinculo_usuario', 'curso']
cadastro_usuarios_depois_2010.columns = ['matricula_ou_siape', 'tipo_vinculo_usuario', 'curso']

# Concatenando os DataFrames dos usuários
cadastro_usuarios_excel = pd.concat([cadastro_usuarios_antes_2010, cadastro_usuarios_depois_2010], ignore_index=True)
cadastro_usuarios_excel['matricula_ou_siape'] = cadastro_usuarios_excel['matricula_ou_siape'].astype('string')

# Leitura dos dados do JSON
try:
    cadastro_usuarios_json = pd.read_json('cadastro_alunos.json')
except FileNotFoundError:
    print("Erro: Arquivo 'cadastro_alunos.json' não encontrado.")
    exit()

# Filtrando apenas os dados de graduação do JSON
cadastro_usuarios_graduacao_json = pd.read_json(cadastro_usuarios_json['registros'][0])
cadastro_usuarios_graduacao_json['matricula_ou_siape'] = cadastro_usuarios_graduacao_json['matricula_ou_siape'].astype('string')

# Concatenando os DataFrames dos usuários
cadastro_usuarios_cursos = pd.concat([cadastro_usuarios_excel, cadastro_usuarios_graduacao_json], ignore_index=True)

# Leitura dos dados de empréstimos
try:
    emprestimos_completo = pd.read_csv('emprestimos_completo_limpo.csv', parse_dates=['data_emprestimo'])
except FileNotFoundError:
    print("Erro: Arquivo 'emprestimos_completo_limpo.csv' não encontrado.")
    exit()

# Filtrando empréstimos de graduação a partir de 2015
matricula_data_de_emprestimo = emprestimos_completo.query("tipo_vinculo_usuario == 'ALUNO DE GRADUAÇÃO'")
matricula_data_de_emprestimo = matricula_data_de_emprestimo.loc[:, ['matricula_ou_siape', 'data_emprestimo']]
matricula_data_de_emprestimo = matricula_data_de_emprestimo.query('data_emprestimo > 2015')
matricula_data_de_emprestimo = matricula_data_de_emprestimo.reset_index(drop=True)

# Excluindo valores nulos de matricula
matricula_data_de_emprestimo = matricula_data_de_emprestimo.dropna()

# Convertendo coluna 'matricula_ou_siape' para tipo string
cadastro_usuarios_cursos['matricula_ou_siape'] = cadastro_usuarios_cursos['matricula_ou_siape'].astype('string')
matricula_data_de_emprestimo['matricula_ou_siape'] = matricula_data_de_emprestimo['matricula_ou_siape'].astype('string')

# Cursos selecionados para análise
cursos_selecionados = ['BIBLIOTECONOMIA', 'CIÊNCIAS SOCIAIS', 'COMUNICAÇÃO SOCIAL', 'DIREITO', 'FILOSOFIA', 'PEDAGOGIA']

# Filtrando empréstimos dos cursos selecionados
try:
    emprestimos_graduacao_2015 = matricula_data_de_emprestimo.merge(cadastro_usuarios_cursos)
    emprestimos_cursos_selecionados = emprestimos_graduacao_2015[emprestimos_graduacao_2015['curso'].isin(cursos_selecionados)]
except KeyError:
    print("Erro: A coluna 'curso' não foi encontrada no DataFrame.")
    exit()

# Agrupando empréstimos por curso e ano
emprestimos_cursos_selecionados['ano'] = emprestimos_cursos_selecionados['data_emprestimo'].dt.year
emprestimos_cursos_selecionados = emprestimos_cursos_selecionados.groupby(['curso', 'ano']).size().reset_index(name='quantidade_emprestimos')

# Pivotando a tabela
emprestimos_pivot = emprestimos_cursos_selecionados.pivot_table(index='curso', columns='ano', values='quantidade_emprestimos', fill_value=0, margins=True, margins_name='Total')

# Exibindo a tabela pivotada
print(emprestimos_pivot)
