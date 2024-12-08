from datetime  import datetime, timedelta
from Modulo import Account, Transaction, CATEGORIES

def test_account_initialization() -> None:
    account = Account(name="Conta Corrente")
    assert account.name == "Conta Corrente"
    assert account.balance == 0.0
    assert account.transactions == []



def test_add_transaction() -> None:
    account = Account(name="Conta Poupança")
    transaction = account.add_transaction(amount=100.0, category=1, description="Pagamento recebido")
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
    account = Account(name="Conta Digital")
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    account.add_transaction(amount=50.0, category=2, description="Depósito 1")
    account.add_transaction(amount=100.0, category=2, description="Depósito 2")
    filtered_transactions = account.get_transactions(start_date=yesterday, end_date=now)
    assert len(filtered_transactions) == 2


def test_get_transactions_category_filter() -> None:
    account = Account(name="Conta Premium")
    account.add_transaction(amount=50.0, category=1, description="Pagamento")
    account.add_transaction(amount=100.0, category=2, description="Depósito")
    filtered_transactions = account.get_transactions(category=1)
    assert len(filtered_transactions) == 1
    assert filtered_transactions[0].category == CATEGORIES[1]


def test_add_transaction_invalid_category() -> None:
    account = Account(name="Conta Estudante")
    try:
        account.add_transaction(amount=50.0, category=99, description="Erro")
    except ValueError as e:
        assert str(e) == "Categoria inválida."