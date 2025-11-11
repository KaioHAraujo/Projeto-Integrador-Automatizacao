import os
import database

DB = "perfect_acqua.db"

if os.path.exists(DB):
    os.remove(DB)
    print("✅ Banco removido")

database.criar_tabelas()
print("✅ Banco recriado com sucesso")
