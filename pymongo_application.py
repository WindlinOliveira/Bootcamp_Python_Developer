import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://windlinoliveira:9910148123@cluster.o7icvzs.mongodb.net/?retryWrites=true&w=majority")

db = client.db_dio

collections = db.bank
print(db.bank)

post_bank = {
    "author": "Windlin",
    "nome_cliente": "Windlin",
    "cpf": "000000000",
    "endereco": "windlin@email.com",
    "conta": {"tipo": "Conta Corrente", "agencia": "00", "num": "11111", "saldo": 10550.60},
    "tags": ["bank", "client", "mongodb", "pymongo"],
    "date": datetime.datetime.utcnow()
}

bank_collection = db.bank
bank_id = bank_collection.insert_one(post_bank).inserted_id


new_posts_bank = [{
    "author": "Windlin",
    "nome_cliente": "Maria",
    "cpf": "000000001",
    "endereco": "majo@email.com",
    "conta": {"tipo": "Conta Corrente", "agencia": "00", "num": "22222", "saldo": 503.23},
    "tags": ["bank", "client", "mongodb", "pymongo"],
    "date": datetime.datetime.utcnow()
    },
    {
        "author": "Windlin",
        "nome_cliente": "Pedro",
        "cpf": "000000002",
        "endereco": "pedro@email.com",
        "conta": {"tipo": "Conta Corrente", "agencia": "00", "num": "33333", "saldo": 23.59},
        "tags": ["bank", "client", "mongodb", "pymongo"],
        "date": datetime.datetime.utcnow()
    },
    {
        "author": "Windlin",
        "nome_cliente": "Ana",
        "cpf": "000000003",
        "endereco": "ana@email.com",
        "conta": {"tipo": "Conta Corrente", "agencia": "00", "num": "44444", "saldo": 100},
        "tags": ["bank", "client", "mongodb", "pymongo"],
        "date": datetime.datetime.utcnow()
    }]

multiple_posts_bank = bank_collection.insert_many(new_posts_bank)
print(multiple_posts_bank)

print("\nRecuperação final")
pprint.pprint(bank_collection.find_one({"nome_cliente": "Pedro"}))

print("\n Documentos presentes na coleção bank")
for post in bank_collection.find():
    pprint.pprint(post)
