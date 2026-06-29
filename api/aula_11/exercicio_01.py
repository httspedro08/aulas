import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
''')

produtos_iniciais = [
    ('Teclado Mecânico', 250.00),
    ('Mouse Gamer', 120.50),
    ('Monitor 24 polegadas', 899.90)
]

cursor.executemany('''
    INSERT INTO produtos (nome, preco)
    VALUES (?, ?)
''', produtos_iniciais)

conn.commit()
conn.close()

print("Banco de dados criado e produtos inseridos com sucesso!")