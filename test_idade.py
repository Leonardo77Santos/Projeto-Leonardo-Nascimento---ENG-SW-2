from idade import idade_permitida


def test_idade_exatamente_no_limite_e_aceita():
    # preparar
    idade = 16
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is True


def test_idade_um_ano_abaixo_do_limite_e_rejeitada():
    # preparar
    idade = 15
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False


def test_idade_acima_de_100_e_rejeitada():
    # preparar
    idade = 101
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False


def test_idade_com_casa_decimal_e_rejeitada():
    # preparar
    idade = 16.5
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False
