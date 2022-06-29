# 基本的な使用方法

import subprocess

# ディレクトリ作成
# subprocess.run('mkdir test', shell=True)

# ファイル情報の取得と出力
cp = subprocess.run(r'dir .\test', shell=True,
                    capture_output=True, text=True)

print(cp.stdout)        # 出力結果
print(cp.returncode)    # returnコードの出力
print(cp.stderr)        # エラコードを出力
