
from datetime import datetime
from typing import Dict, List, Optional

CATEGORIES: Dict[int, str] = {
    1: "Pagamento",
    2: "Depósito",
    3: "Transferência",
}

class Transaction:
    """Classe para representar transações financeiras."""

    def __init__(self, amount: float, category: int, description: str = "") -> None:
        """Inicializa um objeto Transaction.

        Args:
            amount (float): O valor da transação.
            category (int): A categoria da transação.
            description (str, optional): A descrição da transação.
        """

        if category not in CATEGORIES:
            raise ValueError("Categoria inválida.")
        self.amount: float = amount
        self.date: datetime = datetime.now()
        self.category: str = CATEGORIES[category]
        self.description: str = description

    def __str__(self) -> str:
        """Retorna uma descrição da transação."""
        return f"Transação: {self.description} R$ {self.amount:.2f} ({self.category})"

    def update(self, **attributes: dict) -> None:
        """Atualiza um ou mais atibutos da transação.

        Args:
            amount (float, optional): O valor da transação.
            category (int, optional): A categoria da transação.
            description (str, optional): A descrição da transação.
            date (datetime, optional): A data da transação.

        """
        for attr, value in attributes.items():
            if attr == "category" and value not in CATEGORIES:
                raise ValueError("Categoria inválida.")
            setattr(self, attr, CATEGORIES[value] if attr == "category" else value)


class Account:
    """Classe para representar contas e armazenar transações."""

    def __init__(self, name: str) -> None:
        """Inicializa um objeto Account.

        Args:
            name (str): O nome da conta.
        """
        self.name: str = name
        self.balance: float = 0.0
        self.transactions: List[Transaction] = []

    def add_transaction(self, amount: float, category: int, description: str = "") -> Transaction:
        """Cria uma transação na conta e atualiza o saldo da conta.

        Args:
            amount (float): O valor da transação.
            category (int): A categoria da transação.
            description (str, optional): A descrição da transação.

            Returns:
            Transaction: O objeto Transaction criado.
        """
        if category not in CATEGORIES:
            raise ValueError("Categoria inválida.")
        transaction = Transaction(amount, category, description)
        self.balance += amount
        self.transactions.append(transaction)
        self.transactions.sort(key=lambda t: t.date)
        return transaction

    def get_transactions(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, category: Optional[int] = None
    ) -> List[Transaction]:
        """Retorna uma lista de transações entre duas datas.

        Args:
            start_date (datetime, optional): A data de início.
            end_date (datetime, optional): A data de fim.
        Returns:
            list[Transaction]: Uma lista de objetos Transaction.
        """
        return [
            t for t in self.transactions
            if (start_date is None or t.date >= start_date)
            and (end_date is None or t.date <= end_date)
            and (category is None or t.category == CATEGORIES[category])
        ]


class Investment:
    """Classe para representar investimentos."""

    def __init__(self, type: str, initial_amount: float, rate_of_return: float) -> None:
        """Inicializa um objeto Investment.

        Args:
            type (int): O tipo de investimento.
            amount (float): O valor do investimento.
            rate_of_return (float): A taxa de retorno do investimento.
        """
        self.type: str = type
        self.initial_amount: float = initial_amount
        self.date_purchased: datetime = datetime.now()
        self.rate_of_return: float = rate_of_return

    def calculate_value(self, date: Optional[datetime] = None) -> float:
        """Calcula o valor atual do investimento ou para determinada data."""
        date = date or datetime.now()
        meses_passados = (date - self.date_purchased).days // 30
        return self.initial_amount * (1 + self.rate_of_return) ** meses_passados

    def sell(self, account: Account) -> None:
        """Realiza a venda do investimento.

        Args:
            account (Account): A conta onde o investimento será vendido.
        """
        value = self.calculate_value()
        account.add_transaction(value, 2, f"Venda de investimento {self.type}")
        self.initial_amount = 0.0


class Client:
    """Classe para representar clientes."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        """Cria uma nova conta para o cliente.

        Args:
            account_name (str): O nome da conta.

        Returns:
            Account: A conta que foi criada.
        """
        if any(account.name == account_name for account in self.accounts):
            raise ValueError("Conta já existe.")
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        """Adiciona um investimento para o cliente.

        Args:
            investment (Investment): O investimento a ser adicionado.
        """
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """Calcula a soma do valor atual de todas as contas e investimentos do cliente."""
        total_accounts = sum(account.balance for account in self.accounts)
        total_investments = sum(investment.calculate_value() for investment in self.investments)
        return total_accounts + total_investments


def generate_report(client: Client) -> dict:
    """Gera um relatório financeiro com as informações do cliente.

    Args:
        client (Client): O cliente para o qual o relatório será gerado.

    Returns:
        str: O relatório financeiro.
    """
    # Relatório de introdução
    report = f"Relatório Financeiro de {client.name}:\n"
    report += f"Patrimônio Líquido: R$ {client.get_net_worth():.2f}\n\n"
    
    # Relatório de Contas
    report += "Contas:\n"
    for account in client.accounts:
        report += f"- {account.name}: R$ {account.balance:.2f}\n"
    
    report += "\n"
    
    # Relatório de Investimentos
    report += "Investimentos:\n"
    for investment in client.investments:
        report += f"- {investment.type}: R$ {investment.calculate_value():.2f}\n"
    
    return report


def future_value_report(client: Client, future_date: datetime) -> str:
    # Calculando os meses até a data futura
    months_ahead = (future_date - datetime.now()).days // 30
    
    # Iniciando o relatório
    report = [f"Projeção de Rendimentos para {client.name} até {future_date.strftime('%d/%m/%Y')}\n"]
    
    # Projeção de investimentos futuros
    report.append("Investimentos Futuros:")
    for investment in client.investments:
        # Usando o valor inicial do investimento para calcular o valor futuro
        future_value = investment.initial_amount * ((1 + investment.rate_of_return) ** months_ahead)
        report.append(f"- {investment.type}: Valor Projetado R$ {future_value:,.2f}")
    
    # Relatório de contas
    report.append("\nContas:")
    for account in client.accounts:
        report.append(f"- {account.name}: Saldo Atual R$ {account.balance:,.2f}")
    
    # Projeção do patrimônio líquido
    projected_net_worth = client.get_net_worth() + sum(
        investment.initial_amount * ((1 + investment.rate_of_return) ** months_ahead) 
        for investment in client.investments
    )
    report.append(f"\nPatrimônio Líquido Projetado: R$ {projected_net_worth:,.2f}")
    
    # Retorna o relatório em formato de string
    return "\n".join(report)



    