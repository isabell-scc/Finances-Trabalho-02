from setuptools import setup, find_packages

setup(
    name="backend_finances", 
    version="0.1",  
    packages=find_packages(),  # Vai buscar os pacotes automaticamente dentro do diretório
    description="Um gerenciador financeiro com funcionalidades de transações, contas e investimentos.",
    install_requires=[ ],
    author="Maria Rita e Isabel"
)