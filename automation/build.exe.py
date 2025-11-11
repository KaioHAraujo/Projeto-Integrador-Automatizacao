import subprocess

print("🏗  Construindo executável...")
subprocess.call([
    "pyinstaller",
    "--noconfirm",
    "--windowed",
    "--name", "PerfectAcqua",
    "main.py"
])
print("✅ Build finalizado! Arquivo em dist/PerfectAcqua")
