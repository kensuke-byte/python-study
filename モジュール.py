prompt = int(input("プロンプトを選択してください。"))
if prompt == 1:
    # randomモジュール
    import random

    omikuji = ["大吉", "中吉", "小吉", "凶", "大凶"]
    result = random.choice(omikuji)
    print(f"今日の運勢は{result}です。")
else:
    pass


if prompt == 2:
    print("hi")
else:
    pass
