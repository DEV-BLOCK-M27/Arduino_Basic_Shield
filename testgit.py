import subprocess
try:
    result = subprocess.check_output(["git", "--version"], shell=True).strip().decode("utf-8")
    print(f"Git-Version gefunden: {result}")
except FileNotFoundError:
    print("Git ist nicht im PATH verfügbar.")