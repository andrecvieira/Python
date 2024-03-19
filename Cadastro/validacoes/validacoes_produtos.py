def validar_preco(preco):
    try:
        preco_float = float(preco)
        if preco_float <= 0:
            return False
        return True
    except ValueError:
        return False

def validar_nome_produto(nome):
    if not nome.strip():
        return False
    return True