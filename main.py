import pandas as pd

# Add as tabelas com os dados dos 3 mercados por dia para pasta do projeto e depois colocar o nome delas
tabela_10 = pd.read_excel('precosdodia10.xlsx')
tabela_17 = pd.read_excel('precosdodia17.xlsx')
tabela_21 = pd.read_excel('precosdodia21.xlsx')
tabela_2106 = pd.read_excel('precos2106.xlsx')

#funcao para comparar tabelas
def comparar_tabelas(tabela_10, tabela_17, tabela_21, tabela_2106):
    produtos = tabela_10['Produto'].unique()
    dias = ['10', '17', '21', '21/06']
    contagem_dias = {dia: 0 for dia in dias}

    for produto in produtos:
        precos_10 = tabela_10.loc[tabela_10['Produto'] == produto, ['Carrefour', 'Pitico', 'Extra']].values.flatten().tolist()
        precos_17 = tabela_17.loc[tabela_17['Produto'] == produto, ['Carrefour', 'Pitico', 'Extra']].values.flatten().tolist()
        precos_21 = tabela_21.loc[tabela_21['Produto'] == produto, ['Carrefour', 'Pitico', 'Extra']].values.flatten().tolist()
        precos_2106 = tabela_2106.loc[tabela_2106['Produto'] == produto, ['Carrefour', 'Pitico', 'Extra']].values.flatten().tolist()

        menor_preco = min(precos_10 + precos_17 + precos_21 + precos_2106)

        if menor_preco in precos_10:
            contagem_dias['10'] += 1
        if menor_preco in precos_17:
            contagem_dias['17'] += 1
        if menor_preco in precos_21:
            contagem_dias['21'] += 1
        if menor_preco in precos_2106:
            contagem_dias['21/06'] += 1

    dia_mais_barato = max(contagem_dias, key=contagem_dias.get)
    total_produtos = len(produtos)
    porcentagem_dia_mais_barato = (contagem_dias[dia_mais_barato] / total_produtos) * 100

    print(f"A maioria dos produtos estava mais barata no dia {dia_mais_barato}.")
    print(f"{contagem_dias[dia_mais_barato]} produtos ({porcentagem_dia_mais_barato:.2f}%) tiveram o menor preço nesse dia.")

# Chamar a função para comparar as tabelas
comparar_tabelas(tabela_10, tabela_17, tabela_21, tabela_2106)
