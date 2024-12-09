from datetime  import datetime, timedelta
from finances import Account, Transaction, CATEGORIES

def test_account_initialization() -> None:
    """"verificando a correta relação de atributos"""
    account = Account(name="Conta Corrente")
    assert account.name == "Conta Corrente"
    assert account.balance == 0.0
    assert account.transactions == []

def test_add_transaction() -> None:
    """Teste de adição de transação"""
    account = Account(name="Conta Poupança")
    transaction = account.add_transaction(amount=100.0, category=1, description="Pagamento recebido")

    #verificando se as transações estão sendo feitas corretamente e os atributos também
    assert isinstance(transaction, Transaction)
    assert transaction.amount == 100.0
    assert transaction.category == CATEGORIES[1]
    assert transaction.description == "Pagamento recebido"
    assert account.balance == 100.0
    assert len(account.transactions) == 1

    assert isinstance(account.name, str)
    assert isinstance(account.balance, float)
    assert isinstance(account.transactions, list)

def test_get_transactions_date_filter() -> None:
    """verificando as adições das transações juntamente com o momento que ocorreram"""
    account = Account(name="Conta Digital")
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    account.add_transaction(amount=50.0, category=2, description="Depósito 1")
    account.add_transaction(amount=100.0, category=2, description="Depósito 2")
    filtered_transactions = account.get_transactions()
    assert len(filtered_transactions) == 2

def test_get_transactions_category_filter() -> None:
    """verificando as filtragens das transações"""
    account = Account(name="Conta Premium")
    account.add_transaction(amount=50.0, category=1, description="Pagamento")
    account.add_transaction(amount=100.0, category=2, description="Depósito")
    filtered_transactions = account.get_transactions(category=1)
    assert len(filtered_transactions) == 1
    assert filtered_transactions[0].category == CATEGORIES[1]

def test_add_transaction_invalid_category() -> None:
    """verificando a inserção de uma categoria inválida"""
    account = Account(name="Conta Estudante")
    try:
        account.add_transaction(amount=50.0, category=99, description="Erro")
    except ValueError as e:
        assert str(e) == "Categoria inválida."