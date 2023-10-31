"""
Essa API integra com o banco de dados utilizando ORM

"""

from sqlalchemy.orm import (
    declarative_base,
    Session,
    relationship,
)

from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    ForeignKey, Float,
    create_engine, select,
)


Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(VARCHAR)
    cpf = Column(VARCHAR(9), unique=True)
    endereco = Column(VARCHAR)

    conta = relationship(
        'Conta', back_populates='cliente'
    )

    def __repr__(self):
        return f"Cliente (id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco}"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(VARCHAR)
    agencia = Column(VARCHAR)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float)

    cliente = relationship(
        'Cliente', back_populates='conta'
    )

    def __repr__(self):
        return f"Conta (id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo}"


engine = create_engine("sqlite:///:memory:")

Base.metadata.create_all(engine)

with Session(engine) as session:
    windlin = Cliente(
        nome='Windlin',
        cpf='000000000',
        endereco='windlin@email.com',
        conta=[Conta(tipo='Conta Corrente',
                     agencia='00',
                     num='11111',
                     saldo=10550.60)]
    )

    maria = Cliente(
        nome='Maria',
        cpf='000000001',
        endereco='majo@email.com',
        conta=[Conta(tipo='Conta Corrente',
                     agencia='00',
                     num='22222',
                     saldo=503.23)]
    )

    pedro = Cliente(
        nome='Pedro',
        cpf='000000002',
        endereco='pedro@email.com',
        conta=[Conta(tipo='Conta Corrente',
                     agencia='00',
                     num='33333',
                     saldo=23.59)]
    )

    ana = Cliente(
        nome='Ana',
        cpf='000000003',
        endereco='aninha@email.com',
        conta=[Conta(tipo='Conta Corrente',
                     agencia='00',
                     num='44444',
                     saldo=100)]
    )

    session.add_all([windlin, maria, pedro, ana])

    session.commit()

while True:
    print('\n---------------------------------------------------------------------------------------------')
    print('\nEscolha uma opção: ')
    print('1. Recuperar dados do cliente por nome')
    print('2. Recuperar dados da conta por id do cliente')
    print('3. Recuperar dados de cliente de forma ordenada')
    print('4. Recuperar dados de id, nome e saldo')
    print('0. Sair')

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':
        print('\n--------------------- Recuperando os dados do cliente por nome -------------------------------')

        nome_busca = str(input('Digite o nome do cliente: '))
        stmt_nome = select(Cliente).where(Cliente.nome.in_([nome_busca]))
        for cliente in session.scalars(stmt_nome):
            print(cliente)

    elif opcao == '2':
        print('\n------------------- Recuperando os dados da conta pelo ID do cliente--------------------------')

        id_cliente_busca = int(input('Digite o id do cliente: '))
        stmt_conta = select(Conta).where(Conta.id_cliente.in_([id_cliente_busca]))
        for conta in session.scalars(stmt_conta):
            print(conta)

    elif opcao == '3':
        print('\n-------------------Recuperando os dados de cliente de forma ordenada -------------------------')
        stmt_order = select(Cliente).order_by(Cliente.nome)
        for cliente in session.scalars(stmt_order):
            print(cliente)

    elif opcao == '4':
        print('\n--------------------- Recuperando os dados de id, nome e saldo ------------------------------')
        stmt_join = select(Cliente.id, Cliente.nome, Conta.saldo).join_from(Cliente, Conta)
        for result in session.execute(stmt_join):
            print(result)

    elif opcao == '0':
        break
