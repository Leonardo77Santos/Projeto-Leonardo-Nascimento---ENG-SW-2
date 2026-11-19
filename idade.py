MINIMA = 16  # TROQUE pelo seu LIMITE


def idade_permitida(idade):
    if idade > 100:
        return False
    return idade > MINIMA
