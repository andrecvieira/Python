import tkinter as tk
from tkinter import messagebox
from validacoes.validacoes_clientes import validar_nome_cliente, validar_email, validar_cpf, validar_cnpj
from banco_de_dados.database import Database

class InterfaceClientes:
    def __init__(self, container):
        self.container = container
        self.frame = tk.Frame(self.container)
        self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.container.grid_columnconfigure(0, weight=1)

        self.tipo_cliente = tk.StringVar(value="Pessoa Física")
        self.campos_frame = None  # Frame para os campos dinâmicos
        self.campos_entries = {}

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.frame, text="Cadastro de Clientes", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        tk.Radiobutton(self.frame, text="Pessoa Física", variable=self.tipo_cliente, value="Pessoa Física", command=self.atualizar_campos).grid(row=1, column=0)
        tk.Radiobutton(self.frame, text="Pessoa Jurídica", variable=self.tipo_cliente, value="Pessoa Jurídica", command=self.atualizar_campos).grid(row=1, column=1)

        self.atualizar_campos()

    def atualizar_campos(self):
        if self.campos_frame is not None:
            self.campos_frame.destroy()

        self.campos_frame = tk.Frame(self.frame)
        self.campos_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.criar_campos_dinamicos()

    def criar_campos_dinamicos(self):
        campos_labels = {
            "Pessoa Física": ["Nome completo", "CPF", "Data de aniversário", "Profissão", "Endereço completo", "Telefone fixo", "Celular", "Email", "Observações"],
            "Pessoa Jurídica": ["Razão Social", "Nome fantasia", "CNPJ", "Inscrição estadual", "Data da fundação", "Endereço completo", "Telefone fixo", "Celular", "Email", "Observações"]
        }

        self.campos_entries.clear()  # Limpa o dicionário de entradas
        for row, label in enumerate(campos_labels[self.tipo_cliente.get()], start=0):
            tk.Label(self.campos_frame, text=f"{label}:").grid(row=row, column=0, sticky="e", pady=2)
            entry = tk.Entry(self.campos_frame)
            entry.grid(row=row, column=1, sticky="ew", pady=2)
            self.campos_entries[label] = entry

        row = len(campos_labels[self.tipo_cliente.get()])
        tk.Button(self.campos_frame, text="Cadastrar Cliente", command=self.cadastrar_cliente).grid(row=row, column=0, columnspan=2, pady=10)

    def cadastrar_cliente(self):
        tipo_cliente = self.tipo_cliente.get()
        dados_cliente = {campo: entry.get().strip() for campo, entry in self.campos_entries.items()}
        
        if tipo_cliente == "Pessoa Física":
            # Validação para Pessoa Física
            if (not validar_nome_cliente(dados_cliente.get("Nome completo", "")) or
                not validar_cpf(dados_cliente.get("CPF", "")) or
                not validar_email(dados_cliente.get("Email", ""))):
                messagebox.showerror("Erro", "Dados de Pessoa Física inválidos.")
                return False
        else:
            # Validação para Pessoa Jurídica
            if (not validar_nome_cliente(dados_cliente.get("Razão Social", "")) or
                not validar_cnpj(dados_cliente.get("CNPJ", "")) or
                not validar_email(dados_cliente.get("Email", ""))):
                messagebox.showerror("Erro", "Dados de Pessoa Jurídica inválidos.")
                return False
        
        # Se passar pela validação, proceder com o cadastro no banco de dados
        db = Database()
        if tipo_cliente == "Pessoa Física":
            db.inserir_cliente_pf(dados_cliente)  # Assumindo que essa função existe
        else:
            db.inserir_cliente_pj(dados_cliente)  # Assumindo que essa função existe
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso.")
        self.limpar_campos()

    def limpar_campos(self):
        for entry in self.campos_entries.values():
            entry.delete(0, tk.END)

    def mostrar(self):
        self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.container.grid_columnconfigure(0, weight=1)

    def esconder(self):
        self.frame.grid_remove()
