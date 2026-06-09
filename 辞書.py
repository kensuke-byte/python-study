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


# リストの内包表記
if prompt == 7:
    # 基本の形　{キーの計算: 値の計算 for 要素 in データの塊}

    # 通常の書き方
    squares_01 = {}
    for x in range(1, 4):
        squares_01[x] = x**2
        print(squares_01)
        # {1: 1, 2: 4, 3: 9}
    print()

    # リストの内包表記
    squares_02 = {x: x**2 for x in range(1, 4)}
    print(squares_02)
    # {1: 1, 2: 4, 3: 9}
else:
    pass

if prompt == 8:
    weapons = ["木の剣", "石の剣", "鉄の剣"]
    attacks = [5, 8, 12]

    # 武器名を「キー」、攻撃力を「値」にした辞書を1行で作る
    weapon_dict = {w: a for w, a in zip(weapons, attacks)}

    print(weapon_dict)
    # 結果: {'木の剣': 5, '石の剣': 8, '鉄の剣': 12}
else:
    pass

if prompt == 9:
    # 元のデータ（商品名と価格）
    prices = {"リンゴ": 100, "バナナ": 150, "メロン": 800, "イチゴ": 400}

    # 200円以上（高級品）のデータだけを抽出した新しい辞書を作る
    luxury_prices = {name: price for name, price in prices.items() if price >= 200}

    print(luxury_prices)
    # 結果: {'メロン': 800, 'イチゴ': 400}
else:
    pass

if prompt == 10:
    id_to_name = {101: "田中", 102: "佐藤", 103: "鈴木"}

    # キー(k)と値(v)を入れ替えて {v: k} にする
    name_to_id = {v: k for k, v in id_to_name.items()}

    print(name_to_id)
    # 結果: {'田中': 101, '佐藤': 102, '鈴木': 103}
else:
    pass


# ネストしたオブジェクトの構築
if prompt == 11:
    # 1. まずは空の辞書（土台）を作る
    school = {}

    # 2. 「1組」というキーに、空のリストを追加する
    school["1組"] = []

    # 3. そのリストに、生徒の辞書を `.append()` で追加していく
    school["1組"].append({"name": "太郎", "score": 80})
    school["1組"].append({"name": "花子", "score": 95})

    print(school)
    # 結果: {'1組': [{'name': '太郎', 'score': 80}, {'name': '花子', 'score': 95}]}
else:
    pass

if prompt == 12:
    # 元のデータ
    menbers_name = ["田中", "佐藤", "鈴木"]
    jobs = ["戦士", "弓術師", "騎士"]

    # 空の辞書を用意
    game_characters = {}

    # for文とzip()を使って、同時に取り出しながら組み立てる
    for name, job in zip(menbers_name, jobs):
        # 名前をキーにして、中身をさらに辞書にする
        game_characters[name] = {
            "job": job,
            "level": 1,
            "HP": 100,
        }

    print(game_characters)
    # 結果: {'田中': {'job': '戦士', 'level': 1, 'HP': 100}, '佐藤': {'job': '魔法使い', ...}}
else:
    pass

if prompt == 13:
    member_names = ["田中", "佐藤", "鈴木"]
    jobs = ["戦士", "魔法使い", "僧侶"]

    # 1行でネストした辞書を構築
    game_characters = {
        name: {"job": job, "level": 1, "HP": 100}
        for name, job in zip(member_names, jobs)
    }
    print(game_characters)
    # 結果: {'田中': {'job': '戦士', 'level': 1, 'HP': 100}, '佐藤': {'job': '魔法使い', ...}}
else:
    pass
