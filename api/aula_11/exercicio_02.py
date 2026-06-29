import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute('SELECT id, nome, preco FROM produtos')
produtos = cursor.fetchall()

print("--- Lista de Produtos ---")
for produto in produtos:
    id_prod, nome, preco = produto
    print(f"ID: {id_prod} | Nome: {nome} | Preço: R$ {preco:.2f}")

conn.close()