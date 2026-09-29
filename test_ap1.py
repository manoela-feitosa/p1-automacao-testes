#Aluna: Manoela Soares Feitosa 
#Curso: SI 3

from questao_ap1 import *
import pytest

# QUESTÃO 1

def test_imc_baixo():
    assert classificar_imc(17) == "Abaixo do peso"

def test_imc_normal():
    assert classificar_imc(22) == "Peso normal"

def test_imc_alto():
    assert classificar_imc(30) == "Acima do peso"

def test_imc_18_5():
    assert classificar_imc(18.5) == "Peso normal"


# QUESTÃO 2

def test_saque():
    assert sacar(100, 40) == 60

def test_saque_sem_saldo():
    with pytest.raises(ValueError):
        sacar(100, 150)


# QUESTÃO 3

def test_frete_leve():
    assert calcular_frete(3) == 10.0

def test_frete_medio():
    assert calcular_frete(7) == 20.0

def test_frete_pesado():
    assert calcular_frete(15) == 35.0

def test_frete_5():
    assert calcular_frete(5) == 10.0

def test_frete_10():
    assert calcular_frete(10) == 20.0


# QUESTÃO 4

def test_senha_certa():
    assert senha_valida("python123") is True

def test_senha_curta():
    assert senha_valida("abc123") is False

def test_senha_sem_numero():
    assert senha_valida("abcdefgh") is False

def test_senha_8_caracteres():
    assert senha_valida("abcdefg1") is True


# QUESTÃO 5

def test_desconto():
    assert aplicar_desconto(100, 20) == 80

def test_desconto_zero():
    assert aplicar_desconto(100, 0) == 100

def test_desconto_total():
    assert aplicar_desconto(100, 100) == 0

def test_desconto_errado():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 110)


# QUESTÃO 6

def test_media():
    assert calcular_media([8, 7, 9]) == 8

def test_notas_iguais():
    assert calcular_media([7, 7, 7]) == 7

def test_uma_nota():
    assert calcular_media([10]) == 10

def test_sem_notas():
    with pytest.raises(ValueError):
        calcular_media([])
        
        
# Testar a lista vazia é importante para verificar se a função trata
# corretamente a falta de notas e retorna o erro esperado.