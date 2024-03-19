# Arquivo: validacoes_clientes.py

import re

def validar_nome_cliente(nome):
    """
    Função para validar o nome do cliente.
    
    Args:
        nome (str): O nome a ser validado.
        
    Returns:
        bool: True se o nome for válido, False caso contrário.
    """
    # Verifica se o nome possui pelo menos um caractere e não excede 100 caracteres
    return bool(nome) and len(nome) <= 100

def validar_email(email):
    """
    Função para validar o email do cliente.
    
    Args:
        email (str): O email a ser validado.
        
    Returns:
        bool: True se o email for válido, False caso contrário.
    """
    # Verifica se o email possui pelo menos um @
    return '@' in email

def validar_cpf(cpf):
    """
    Função para validar o CPF do cliente.
    
    Args:
        cpf (str): O CPF a ser validado.
        
    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    cpf = re.sub('[^0-9]', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 11 or cpf == '00000000000':
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True

def validar_cnpj(cnpj):
    """
    Função para validar o CNPJ do cliente.
    
    Args:
        cnpj (str): O CNPJ a ser validado.
        
    Returns:
        bool: True se o CNPJ for válido, False caso contrário.
    """
    cnpj = re.sub('[^0-9]', '', cnpj)  # Remove caracteres não numéricos
    if len(cnpj) != 14 or cnpj == '00000000000000':
        return False
    multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * multiplicadores[i]
    resto = soma % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto
    if digito_verificador1 != int(cnpj[12]):
        return False
    multiplicadores.insert(0, 6)
    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * multiplicadores[i]
    resto = soma % 11
    if resto < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto
    if digito_verificador2 != int(cnpj[13]):
        return False
    return True
