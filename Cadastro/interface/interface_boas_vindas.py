import tkinter as tk

class InterfaceBoasVindas:
    def __init__(self, container):
        self.container = container
        self.frame = tk.Frame(self.container)
        self.label_welcome = tk.Label(self.frame, text="Bem-vindo ao Sistema de Cadastro", font=("Arial", 20))
        self.label_welcome.pack(pady=20)

    def mostrar(self):
        self.frame.grid(row=0, column=0, sticky="nsew")

    def esconder(self):
        self.frame.grid_forget()
