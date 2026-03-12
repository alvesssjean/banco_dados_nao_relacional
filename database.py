from pymongo import MongoClient

connection_string = "mongodb://mongodb:27018"

try:

    client = MongoClient(connection_string)

    client.admin.command("ping")
    
    db = client["nomedadatabase"]

    colecao = db["users"]
    
    print("Conexão estabelecida com sucesso!")
    


except Exception as e:
    print(f"Erro ao conectar: {e}")
