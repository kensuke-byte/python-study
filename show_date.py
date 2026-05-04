from datetime import datetime

current_date = datetime.now()
print(f"現在の日付: {current_date.strftime('%Y年%m月%d日')}")
print(f"Current date: {current_date.strftime('%Y-%m-%d')}")
print(f"詳細: {current_date.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
