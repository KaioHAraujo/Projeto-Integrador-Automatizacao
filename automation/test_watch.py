import time
import subprocess
import os

last_mtime = {}

def has_changes():
    changed = False
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                mtime = os.path.getmtime(path)
                if path not in last_mtime or last_mtime[path] != mtime:
                    last_mtime[path] = mtime
                    changed = True
    return changed

print("👀 Monitorando alterações...")

while True:
    if has_changes():
        print("🔄 Mudança detectada → rodando testes...")
        subprocess.call(["pytest", "-q"])
    time.sleep(1)
