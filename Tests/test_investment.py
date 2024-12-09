
from datetime import datetime, timedelta
from finances import Investment, Account, Client


def test_investment_initialization():
    """Teste de inicialização do investimento"""
    investimento = Investment("Ações", 1000.0, 0.05)

    # Verificando se os atributos foram inicializados corretamente
    assert investimento.type == "Ações"
    assert investimento.initial_amount == 1000.0
    assert isinstance(investimento.date_purchased, datetime)
    assert investimento.rate_of_return == 0.05

def test_calculate_value():
    """Teste de cálculo do valor do investimento"""
    investimento = Investment(2, 1000.0, 0.05)

    # Simulando 6 meses passados
    investimento.date_purchased -= timedelta(days=180)

    valor_calculado = investimento.calculate_value()
    valor_esperado = 1000.0 * (1 + 0.05) ** 6 #JUROS COMPOSTYOS

    # Verificando se o valor calculado está correto
    assert round(valor_calculado, 2) == round(valor_esperado, 2)


def test_investment_sell():
    """Teste de cálculo do valor do investimento após a venda"""
    cliente = Client("João")
    conta = cliente.add_account("Conta Teste")
    investimento = Investment("Ações", 1000.0, 0.05)
    
    # Simular passagem de tempo
    investimento.date_purchased -= timedelta(days=180)
    
    investimento.sell(conta)
    
    # Verificar se o valor foi adicionado à conta
    assert conta.balance > 0