import tkinter as tk
from interface.interface_clientes import InterfaceClientes
from interface.interface_produtos import InterfaceProdutos
from interface.interface_boas_vindas import InterfaceBoasVindas

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro")
        self._configurar_janela()

        self.frame_principal = tk.Frame(self)
        self.frame_principal.grid(padx=20, pady=20, sticky="nsew")

        self.interface_boas_vindas = InterfaceBoasVindas(self.frame_principal)
        self.interface_clientes = InterfaceClientes(self.frame_principal)
        self.interface_produtos = InterfaceProdutos(self.frame_principal)

        # Certifique-se de que as interfaces de clientes e produtos estão inicialmente escondidas
        self.interface_clientes.esconder()
        self.interface_produtos.esconder()

        self.criar_menu()
        # Mostra apenas a interface de boas-vindas ao iniciar
        self.interface_boas_vindas.mostrar()

    def _configurar_janela(self):
        largura_janela = 800
        altura_janela = 600
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        posicao_x = (largura_tela - largura_janela) // 2
        posicao_y = (altura_tela - altura_janela) // 2
        self.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

    def criar_menu(self):
        menu_lista = tk.Menu(self)
        self.config(menu=menu_lista)

        menu_principal = tk.Menu(menu_lista, tearoff=0)
        menu_lista.add_cascade(label="Menu", menu=menu_principal)
        menu_principal.add_command(label="Boas Vindas", command=self.mostrar_boas_vindas)
        menu_principal.add_command(label="Cadastro de Clientes", command=self.mostrar_clientes)
        menu_principal.add_command(label="Cadastro de Produtos", command=self.mostrar_produtos)
        menu_principal.add_separator()
        menu_principal.add_command(label="Sair", command=self.quit)

    def mostrar_boas_vindas(self):
        self.interface_clientes.esconder()
        self.interface_produtos.esconder()
        self.interface_boas_vindas.mostrar()

    def mostrar_clientes(self):
        self.interface_boas_vindas.esconder()
        self.interface_produtos.esconder()
        self.interface_clientes.mostrar()

    def mostrar_produtos(self):
        self.interface_boas_vindas.esconder()
        self.interface_clientes.esconder()
        self.interface_produtos.mostrar()

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
