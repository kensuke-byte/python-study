prompt = int(input("数値を入力してプロンプトを選択してください。"))
if prompt == 1:
    d = {"東京": "Tokyo", "大阪": "Osaka", "京都": "Kyoto"}
    print(d)
    print(type(d))
    print(d["東京"])
    print("東京" in d)
    print("京都" not in d)
    d["京都"] = "KYOTO"
    print(d)
    del d["東京"]
    print(d)
    d.get("栃木")
    print(type(d.get("栃木")))
    print(d.get("栃木") is None)
else:
    pass

if prompt == 2:
    score = {"数学": 80, "英語": 75}
    print(score)

    # 追加・変更
    score["国語"] = 90  # 新しいキーなら追加
    score["数学"] = 85  # 既存のキーなら変更
    print(score)

    # 削除
    del score["英語"]
    print(score)
else:
    pass

if prompt == 3:
    user = {"名前": "田中", "年齢": 25, "性別": "男性"}

    # 1.キーだけ欲しいとき、keys()を使う
    for key in user:
        print(key)  # 名前、年齢、性別
    print()

    # 2.値だけ欲しいとき、values()を使う
    for value in user.values():
        print(value)  # 田中、25、男性
    print()

    # 3.キーと値両方同時にほしいとき、items()を使う
    for key, value in user.items():
        print(f"{key}は{value}です。")  # 名前は田中です。年齢は25です。性別は男性です。
    print()
else:
    pass


# タプルをキーとする辞書
if prompt == 4:
    # (x座標, y座標)：そこにあるオブジェクト
    game_map = {(0, 0): "ローマの城", (1, 2): "宝箱", (3, 5): "ボス"}

    # 座標(1,2)にあるものを取り出す
    print(game_map[(1, 2)])
else:
    pass

if prompt == 5:
    # (姓, 名)：年齢
    user = {("田中", "太郎"): 25, ("佐藤", "太郎"): 30, ("田中", "花子"): 20}

    # 「田中　太郎」の年齢を取り出す
    print(user[("田中", "太郎")])  # 25
else:
    pass


# ネストした辞書
if prompt == 6:
    # 辞書の中にさらに辞書が入っている
    user = {
        "user_01": {"name": "田中", "age": 25, "gender": "男性", "role": "admin"},
        "user_02": {"name": "佐藤", "age": 30, "gender": "男性", "role": "user"},
        "user_03": {"name": "田中", "age": 20, "gender": "男性", "role": "user"},
    }
    # １．まず「user_01」をの辞書を取り出す
    print(user["user_01"])

    # ２．「user_01」の、さらに「name」を取り出す
    print(user["user_01"]["name"])

    # ３．「user_02」の年齢を31歳に変更する
    user["user_02"]["age"] = 31
    print(user["user_02"]["age"])
else:
    pass
