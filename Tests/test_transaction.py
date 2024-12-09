
from datetime import datetime
from finances import Transaction, CATEGORIES


def test_iniciar_transacao():
    """Teste de criação da transação"""
    transacao = Transaction(amount=100.0, category=1, description="Pagamento de serviço")

    # Conferir se o objeto foi instanciado corretamente
    assert isinstance(transacao, Transaction)

    # Conferir se os atributos possuem os valores e tipos corretos
    assert transacao.amount == 100.0
    assert transacao.category == "Pagamento"
    assert transacao.description == "Pagamento de serviço"

    assert isinstance(transacao.amount, float)  
    assert isinstance(transacao.date, datetime) 
    assert isinstance(transacao.category, str)   
    assert isinstance(transacao.description, str)  

def test_impressao_transacao():
    """Teste de impressão no formato correto"""
    transacao = Transaction(amount=50.0, category=2, description="Depósito de dinheiro")
    assert str(transacao) == "Transação: Depósito de dinheiro R$ 50.00 (Depósito)"

def test_update_transacao():
    """Teste do método update para atualizar atributos"""
    transacao = Transaction(amount=150.0, category=3, description="Transferência bancária")

    # Atualizando a transação
    transacao.update(amount=200.0, category=1, description="Pagamento de fatura")

    # Conferir se os atributos foram atualizados corretamente
    assert transacao.amount == 200.0
    assert transacao.category == "Pagamento"
    assert transacao.description == "Pagamento de fatura"


