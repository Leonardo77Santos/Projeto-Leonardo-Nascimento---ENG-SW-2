MINIMA = 16  # TROQUE pelo seu LIMITE


def idade_permitida(idade):
    if not isinstance(idade, int):
        return False
    if idade > 100:
        return False
    return idade >= MINIMA
