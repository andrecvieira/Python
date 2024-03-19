import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('dados.db')
        self.criar_tabela_clientes()  # Criar tabela de clientes
        self.criar_tabela_produtos()  # Criar tabela de produtos

    def criar_tabela_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo TEXT NOT NULL,
                        nome TEXT,
                        cpf_cnpj TEXT,
                        data_aniversario TEXT,
                        profissao TEXT,
                        primeiro_contato TEXT,
                        endereco TEXT,
                        telefone_fixo TEXT,
                        celular TEXT,
                        email TEXT,
                        observacoes TEXT,
                        data_inclusao TEXT)''')
        self.conn.commit()

    def criar_tabela_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL)''')
        self.conn.commit()

    def inserir_cliente_pf(self, cliente_data):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO clientes (tipo, nome, cpf_cnpj, data_aniversario, profissao, primeiro_contato, endereco, telefone_fixo, celular, email, observacoes, data_inclusao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
            cliente_data['Tipo de cliente'],
            cliente_data['Nome completo'],
            cliente_data['CPF/CNPJ'],
            cliente_data['Data de aniversário'],
            cliente_data['Profissão'],
            cliente_data['Primeiro canal de contato'],
            cliente_data['Endereço completo'],
            cliente_data['Telefone fixo'],
            cliente_data['Celular'],
            cliente_data['Email'],
            cliente_data['Observações/Comentários'],
            cliente_data['Data de inclusão']
        ))
        self.conn.commit()

    def inserir_produto(self, nome, preco):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO produtos (nome, preco) VALUES (?, ?)''', (nome, preco))
        self.conn.commit()
