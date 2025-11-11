import subprocess

def run():
    print("✅ Executando suite de testes...")
    resultado = subprocess.call(["pytest", "-vv"])
    if resultado == 0:
        print("✅ Todos os testes passaram!")
    else:
        print("❌ Alguns testes falharam.")

if __name__ == "__main__":
    run()
