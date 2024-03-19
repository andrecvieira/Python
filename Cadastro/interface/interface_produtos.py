import tkinter as tk
from tkinter import messagebox
from validacoes.validacoes_produtos import validar_nome_produto, validar_preco
from banco_de_dados.database import Database

class InterfaceProdutos:
    def __init__(self, container):
        self.container = container
        self.frame = tk.Frame(self.container)

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.frame, text="Cadastro de Produtos", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, sticky="ew", pady=5)

        tk.Label(self.frame, text="Nome do Produto:").grid(row=1, column=0, sticky="e", pady=2)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=1, column=1, sticky="ew", pady=2)

        tk.Label(self.frame, text="Preço:").grid(row=2, column=0, sticky="e", pady=2)
        self.entry_preco = tk.Entry(self.frame)
        self.entry_preco.grid(row=2, column=1, sticky="ew", pady=2)

        tk.Button(self.frame, text="Cadastrar Produto", command=self.cadastrar_produto).grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()

        if not validar_nome_produto(nome) or not validar_preco(preco):
            messagebox.showerror("Erro", "Dados do produto inválidos.")
            return

        db = Database()
        db.inserir_produto(nome, preco)
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso.")
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def mostrar(self):
        self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.container.grid_columnconfigure(0, weight=1)

    def esconder(self):
        self.frame.grid_remove()
