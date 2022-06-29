# windows向けpowershellを使用する

import subprocess

cp = subprocess.run(
    r'powershell -Command "ls C:\Users"',
    shell=True,
    text=True,
    capture_output=True
)

print(cp.stdout)