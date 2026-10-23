from pathlib import Path
import subprocess

log = Path("contribution-log.txt")

def git(*args):
    subprocess.run(["git", *args], check=True)

for day in range(30):
    with log.open("a", encoding="utf-8") as file:
        file.write(f"Project update {day + 1}\n")
    git("add", "contribution-log.txt")
    git("commit", "-m", f"Project log update {day + 1}")

print("30 commits created!")
PY