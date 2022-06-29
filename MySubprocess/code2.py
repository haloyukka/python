# タイムアウト

import subprocess

try:
    subprocess.run(
        'echo start && choice && echo end',
        shell=True,
        timeout=2
    )
except subprocess.TimeoutExpired:
    print('タイムアウトしました')