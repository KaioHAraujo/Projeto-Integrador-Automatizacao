import subprocess
import os

def run():
    print("🧪 Rodando testes e gerando relatório...")
    cmd = ["pytest", "--html=report.html", "--self-contained-html", "-vv"]
    subprocess.call(cmd)
    print("✅ Relatório gerado: report.html")

if __name__ == "__main__":
    run()
