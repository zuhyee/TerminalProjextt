from datetime import date, timedelta
import subprocess

start = date.today() - timedelta(days=364)
end = date.today()
current = start

while current <= end:
    print(current)
    current += timedelta(days=1)

print("Preview complete. No commits created.")
