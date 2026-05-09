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

if prompt == 2:
    pasword = input("パスワードを入力してください。：")
    if len(pasword) >= 8:
        print("ok")
    else:
        print("no")

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

if prompt == 4:
    a = [0, 1, 4, 9, 16, 25, 36, 49]
    for x in a:
        print(x)

if prompt == 5:
    foods = ["パスタ", "カレー", "唐揚げ"]
    for item in foods:
        print(f"{item}をおいしく食べました。")


# enumerate（エニュメレート）: 「数え上げる」という意味。→ 番号が出る。
if prompt == 6:
    foods = ["パスタ", "カレー", "唐揚げ"]
    for i, item in enumerate(foods, start=1):
        # iには番号、itemには中身が入る。
        print(f"{i}番目のメニューは{item}です。")


# zip（ジップ）: 「チャックを閉める」という意味。→ 2つを合体させる。
if prompt == 7:
    names = ["コーヒー", "紅茶"]
    prices = [400, 450]

    for name, price in zip(names, prices):
        print(f"{name}は{price}円です。")

    for name, price in zip(names, prices):
        print(name, price)

if prompt == 8:
    wd = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    print(wd)
    print(wd[1])

if prompt == 9:
    todo = ["買い物"]
    todo.append("掃除")  # ["買い物", "掃除"]
    todo.insert(0, "散歩")  # ["散歩", "買い物", "掃除"] (0番目に割り込み)
    print(todo)

if prompt == 10:
    colors = ["赤", "青", "黄"]
    colors[1] = "緑"  # 1番目（青）を「緑」に上書き
    # 結果: ["赤", "緑", "黄"]
    print(colors)

if prompt == 11:
    drinks = ["紅茶", "コーヒー", "ミルク"]
    last_item = drinks.pop()  # ミルクを取り出して削除
    drinks.remove("紅茶")  # 紅茶を取り出して削除
    print(drinks)

if prompt == 12:
    japanese = ["い", "う", "あ", "え", "お"]
    japanese.sort()
    """sort(): 中身を小さい順（あいうえお順）に並べ替える。"""
    print(japanese)

if prompt == 13:
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number.reverse()
    """reverse(): 今の並びを真逆にひっくり返す。"""
    print(number)

if prompt == 14:
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number.reverse()
    """index(値): 指定した値が「何番目にあるか」を調べる。"""
    print(number.index(5))

if prompt == 15:
    wd = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    sorted(wd, reverse=True)
    print(wd)

if prompt == 16:
    wd = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    sorted(wd, key=lambda x: len(x))
    print(wd)
