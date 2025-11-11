import shutil
import os

pastas = ["__pycache__", "build", "dist"]
arquivos = ["PerfectAcqua.spec"]

for p in pastas:
    if os.path.exists(p):
        shutil.rmtree(p)
        print(f"🗑  Removido: {p}")

for a in arquivos:
    if os.path.exists(a):
        os.remove(a)
        print(f"🗑  Removido: {a}")

print("✅ Limpeza concluída")
