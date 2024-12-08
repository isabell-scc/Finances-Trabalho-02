from Modulo  import Client, Account, Investment

from  datetime import datetime, timedelta

# Teste de inicialização do objeto Client
def test_inicializacao_cliente():
    cliente = Client(name="João")

    assert cliente.name == "João"
    assert isinstance(cliente.accounts, list)
    assert isinstance(cliente.investments, list)
    assert cliente.accounts == []
    assert cliente.investments == []

# Teste de criação de uma nova conta
def test_adicionar_conta():
    cliente = Client("Maria")
    conta = cliente.add_account("Conta Corrente")

    assert len(cliente.accounts) == 1
    assert isinstance(conta, Account)
    assert conta.name == "Conta Corrente"

# Teste de adicionar um investimento
def test_adicionar_investimento():
    cliente = Client(name="Carlos")
    investimento = Investment("Ações",1000.0, 0.02)
    cliente.add_investment(investimento)

    assert len(cliente.investments) == 1
    assert isinstance(cliente.investments[0], Investment)
    assert cliente.investments[0].type == "Ações"

# Teste de cálculo do patrimônio líquido (net worth)
def test_calcular_patrimonio_liquido():
    cliente = Client(name="Ana")

    # Criando uma conta com saldo
    conta = cliente.add_account("Poupança")
    conta.balance = 2000.0  # Simulando saldo

    # Criando um investimento com retorno
    investimento = Investment(type="Fundos", initial_amount=1000.0, rate_of_return=0.01)
    investimento.date_purchased -= timedelta(days=60)  # Simulando 2 meses passados
    cliente.add_investment(investimento)

    patrimonio = cliente.get_net_worth()
    valor_investimento = 1000.0 * (1 + 0.01) ** 2  # Valor esperado do investimento

    assert round(patrimonio, 2) == round(2000.0 + valor_investimento, 2)

# Teste de atualização dos atributos
def test_atualizacao_atributos():
    cliente = Client(name="Pedro")
    cliente.name = "Pedro Silva"

    assert cliente.name == "Pedro Silva"