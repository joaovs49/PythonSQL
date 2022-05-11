import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-Q0ONR2R;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem sucedida")

cursor = conexao.cursor()
op = input("Operação: ")
id = input("ID: ")
cliente = input(" Cliente:  ")
produto = input("Produto:   ")
data_venda = input("Data Venda:  ")
preco = input("Preço: ")
quantidade = input("Quantidade:   ")

comando = f"""{op} Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ('{id}', '{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()

