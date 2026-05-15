prompt = int(input("数値を入力してプロンプトを選択してください。"))
if prompt == 1:
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a)
    print(type(a))
    print(a[0], a[4])
    print(len(a))
    print(a[2:5])
    print(a[3:])
    print(a[:3])
    print(a[:])
    print(a[-1])
    print(a[2::4])
    print(a[4::-1])
else:
    pass

if prompt == 2:
    pasword = input("パスワードを入力してください。：")
    if len(pasword) >= 8:
        print("ok")
    else:
        print("no")
else:
    pass


if prompt == 3:
    a = [0, 1, 4, 9, 16, 25, 36, 49]
    print(a[2:5])
    print(a[3:])
    print(a[:3])
    print(a[:])
    print(a[-1])
    print(a[2::4])
    print(a[4::-1])
    print(a[5:2:-1])
    print(a[::-1])
else:
    pass

if prompt == 4:
    a = [0, 1, 4, 9, 16, 25, 36, 49]
    for x in a:
        print(x)
else:
    pass


if prompt == 5:
    foods = ["パスタ", "カレー", "唐揚げ"]
    for item in foods:
        print(f"{item}をおいしく食べました。")
else:
    pass


# enumerate（エニュメレート）: 「数え上げる」という意味。→ 番号が出る。
if prompt == 6:
    foods = ["パスタ", "カレー", "唐揚げ"]
    for i, item in enumerate(foods, start=1):
        # iには番号、itemには中身が入る。
        print(f"{i}番目のメニューは{item}です。")
else:
    pass


# zip（ジップ）: 「チャックを閉める」という意味。→ 2つを合体させる。
if prompt == 7:
    names = ["コーヒー", "紅茶"]
    prices = [400, 450]

    for name, price in zip(names, prices):
        print(f"{name}は{price}円です。")

    for name, price in zip(names, prices):
        print(name, price)
else:
    pass


if prompt == 8:
    wd = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    print(wd)
    print(wd[1])
else:
    pass


if prompt == 9:
    todo = ["買い物"]
    todo.append("掃除")  # ["買い物", "掃除"]
    todo.insert(0, "散歩")  # ["散歩", "買い物", "掃除"] (0番目に割り込み)
    print(todo)
else:
    pass


if prompt == 10:
    colors = ["赤", "青", "黄"]
    colors[1] = "緑"  # 1番目（青）を「緑」に上書き
    # 結果: ["赤", "緑", "黄"]
    print(colors)
else:
    pass


if prompt == 11:
    drinks = ["紅茶", "コーヒー", "ミルク"]
    last_item = drinks.pop()  # ミルクを取り出して削除
    drinks.remove("紅茶")  # 紅茶を取り出して削除
    print(drinks)
else:
    pass


if prompt == 12:
    japanese = ["い", "う", "あ", "え", "お"]
    japanese.sort()
    """sort(): 中身を小さい順（あいうえお順）に並べ替える。"""
    print(japanese)
else:
    pass


if prompt == 13:
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number.reverse()
    """reverse(): 今の並びを真逆にひっくり返す。"""
    print(number)
else:
    pass


if prompt == 14:
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number.reverse()
    """index(値): 指定した値が「何番目にあるか」を調べる。"""
    print(number.index(5))
else:
    pass


if prompt == 15:
    wd = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    sorted(wd, reverse=True)
    print(wd)
else:
    pass


if prompt == 16:
    wd = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    sorted(wd, key=lambda x: len(x))
    print(wd)
else:
    pass


if prompt == 17:
    furits = ["banana", "apple", "watermellon"]
    # appleはfuritsの中にあるか
    print("apple" in furits)  # True
    print("orange" in furits)  # False
else:
    pass


if prompt == 18:
    banned_user = ["unknown", "Mr_becon", "merie"]
    print("Faker" not in banned_user)  # True
else:
    pass


if prompt == 19:
    banned_player = ["unknown", "Mr_becon", "merie"]
    user = print(input("あなたのプレイヤーネームは何ですか。："))
    if user not in banned_player:
        print("ログイン可能です。")
    else:
        print("あなたのアカウントは禁止されました。")
else:
    pass


if prompt == 20:

    def caluculate_sum(numbers):
        total = sum(numbers)
        return total

    my_list = [1, 2, 3, 4, 5]
    # リストを丸ごと渡す
    print(caluculate_sum(my_list))  # 15
else:
    pass


if prompt == 21:

    def greet(First, second, third):
        print(f"こんにちは。{First}さん、{second}さん、{third}さん！")

    members = ["田中", "鈴木", "佐藤"]
    # 普通に渡すと「引数が足りない」と怒られるが、
    # * をつけると中身を1人ずつバラして渡してくれる
    greet(*members)
else:
    pass


if prompt == 22:

    def add_all(*args):
        # args は (1, 2, 3) というひとまとめのデータになっている
        return sum(args)

    print(add_all(1, 2, 3))  # 6
else:
    pass


if prompt == 23:
    # 通常の書き方
    numbers = [1, 2, 3]
    doubled = []
    for n in numbers:
        doubled.append(n * 2)
    print(doubled)

    # 内包表記
    doubled = [n * 2 for n in numbers]
    print(doubled)
else:
    pass


if prompt == 24:
    names = ["tanaka", "sato", "suzuki"]
    # 内包表記で大文字に変換
    upper_names = [name.upper() for name in names]
    print(upper_names)
else:
    pass
