import argparse

# メインの引数パーサの設定
parser = argparse.ArgumentParser(prog="expense-tracker", description="Manage your expenses easily")

# サブコマンド用のサブパーサを作成
subparsers = parser.add_subparsers(help="サブコマンドのヘルプ")

# addサブコマンドの設定
add_parser = subparsers.add_parser("add", help="出費を追加する")
add_parser.add_argument("--description", required=True, help="出費の説明")
add_parser.add_argument("--amount", type=int, required=True, help="出費の金額")

# 引数の解析
args = parser.parse_args()
