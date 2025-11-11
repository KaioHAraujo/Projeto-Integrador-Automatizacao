import subprocess

print("🔄 Resetando banco...")
subprocess.call(["python", "reset_db.py"])

print("🧪 Rodando testes...")
result = subprocess.call(["pytest", "-vv"])

if result != 0:
    print("❌ Testes falharam. Build abortado.")
    exit(1)

print("✅ Testes OK — construindo o executável...")
subprocess.call(["python", "build_exe.py"])
