#pandas
import pandas as pd
df_lojas = pd.DataFrame("C:\Users\Mandy\Documents\checkpoint2-Pyhon/lojas.xlsx")
df_lojas = df_lojas.rename(columns={"Código da loja": "Cod_loja", "Nome da loja": "Nome_loja"})

df_produtos = pd.DataFrame(data=produtos)
df_produtos = df_produtos.rename(columns={"Código do produto": "Cod_prod", "Nome do produto": "Nome_Produto", "Código da loja" : "Cod_loja", "preço" : "preco"})



def listar_lojas():
    print("------------------------------------------\n"
          "LOJAS CADASTRADAS\n"
          "__________________________________________")

    print(df_lojas.to_string(index=False))
    print("------------------------------------------\n")
    print("--------------------------------------------------------------------------------\n")

def listar_produtos():
    print("--------------------------------------------------------------------------------\n"
          "PRODUTOS CADASTRADOS\n"
          "________________________________________________________________________________")
    print(df_produtos.to_string(index=False))
    print("--------------------------------------------------------------------------------\n")


def produtos_loja():
    print("------------------------------------------\n"
          "Relatório Produto por Loja\n")

    for value in df_lojas.sort_values(by='Nome_loja').itertuples():
        codLoja = str(value.Cod_loja)
        nomeLoja = str(value.Nome_loja)
        print("-------------------------------------------------------------")
        print(codLoja + " - " + nomeLoja)
        pd.options.display.float_format = '{:,.2f}'.format
        df_produtos_filtro = df_produtos.loc[df_produtos['Cod_loja'] == int(value.Cod_loja)][['Nome_Produto', 'preco']]
        produtos = df_produtos_filtro.to_string(header=False, index=False)
        print(produtos)

    print("\n")


def menu():

    escolha = ' '
    while (escolha != '4'):

        print('\n-----------------------------------\n'
              'MENU - LOJA E PRODUTOS:\n'
              '-----------------------------------\n'
              '1 - Listar Lojas\n'
              '2 - Listas Produtos\n'
              '3 - Relatório - Produtos por loja\n'
              '4 - Sair\n'
              '-----------------------------------')

        escolha = input("Digite uma opção: ")

        if (escolha == '1'):
            listar_lojas()

        elif (escolha == '2'):
            listar_produtos()

        elif (escolha == '3'):
            produtos_loja()

menu()