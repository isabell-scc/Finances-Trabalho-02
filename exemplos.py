from finances import Client, Account, Investment, generate_report, future_value_report
from datetime import datetime, timedelta

# Criando o cliente
cliente = Client("João Silva")

# Adicionando contas
conta_poupanca = cliente.add_account("Poupança")
conta_corrente = cliente.add_account("Corrente")

# Realizando transações nas contas
conta_poupanca.add_transaction(1000.0, 1, "Depósito inicial na poupança")  # Pagamento
conta_corrente.add_transaction(2000.0, 2, "Depósito inicial na corrente")  # Depósito
conta_poupanca.add_transaction(-200.0, 3, "Transferência para a corrente")  # Transferência

# Adicionando investimentos
investimento_imobiliario = Investment("Imobiliário", 5000.0, 0.05)  # Taxa de retorno de 5% ao mês
investimento_tesouro = Investment("Tesouro", 2000.0, 0.03)  # Taxa de retorno de 3% ao mês
cliente.add_investment(investimento_imobiliario)
cliente.add_investment(investimento_tesouro)

# Gerando relatório financeiro atual
relatorio_atual = generate_report(cliente)
print(relatorio_atual)

# Gerando relatório de projeção de rendimentos para daqui a 6 meses
future_date = datetime.now() + timedelta(days=180)
relatorio_futuro = future_value_report(cliente, future_date)
print("\nProjeção de Rendimentos para 6 meses a partir de hoje:")
print(relatorio_futuro)

