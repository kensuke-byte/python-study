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
