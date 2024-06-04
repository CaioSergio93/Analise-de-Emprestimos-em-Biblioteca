import pandas as pd

# Dados do percentual
data = {
    'Curso': ['Administração', 'Arquitetura e Urbanismo', 'Artes Cênicas', 'Bioinformática', 'Bioquímica', 
              'Ciência e Engenharia de Materiais', 'Ciência, Tecnologia e Inovação', 'Ciências da Saúde', 
              'Ciências Odontológicas', 'Design', 'Engenharia Civil', 'Engenharia de Software', 'Filosofia', 
              'Gestão da Informação e do Conhecimento'],
    '2018': [-8.75, -13.22, -1.56, -12.60, -15.26, -8.89, -2.07, -18.41, 5.22, -19.10, -12.92, -10.29, -5.62, -16.55],
    '2019': [-26.94, -5.16, -12.97, -4.65, 5.81, -4.83, -14.33, -8.11, -15.98, 0.16, -4.79, -15.08, -13.43, -6.35],
    '2022': [-84.10, -85.86, -87.36, -85.59, -86.78, -83.67, -85.04, -87.18, -83.51, -86.20, -87.23, -86.01, -82.97, -85.77]
}

# Criando DataFrame
percentual = pd.DataFrame(data)

# Gerando tabela em HTML
html_table = percentual.style.text_gradient(cmap='RdYlGn', low=1, axis=1, vmax=0.1, vmin=0)\
                         .format('{:.2f} %', subset=['2018', '2019', '2022'])\
                         .set_table_styles([{'selector': 'td', 'props': 'font-weight: bold;'}, 
                                            {'selector': 'th', 'props': 'font-weight: bold; background-color: #f2f2f2;'}])\
                         .to_html(classes='styled-table')

# Salvando tabela em um arquivo HTML
with open('tabela.html', 'w') as file:
    file.write(html_table)
