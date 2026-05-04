prompt = int(input("プロンプトの振り分けした値を入力してください。"))
if prompt == 1:
    x: int = 20
    print(x)

if prompt == 2:
    for i in range(10):
        print(i, end="")

if prompt == 3:
    for i in range(1, 10):
        print(i, 1089 * i)

if prompt == 4:
    s = 0
    for i in range(1, 11):
        s += i
    print(s)

if prompt == 5:
    for i in range(10):
        print("w", end="")

if prompt == 6:
    s = 0
    for i in range(1, 21, 2):
        s += i
        print(i, s)

if prompt == 7:
    n = int(input("文字を入れてください。："))
    if n == 1 or n == 6 or n == 8 or n == 10:
        s = "ぽん"
    elif n == 3:
        s = "ぽん"
    else:
        n = "ぽん"
    print(s)

if prompt == 8:
    n = int(input("数値を入れてください。："))
    s = "偶数" if n % 2 == 0 else "奇数"
    print(s)

if prompt == 9:
    while True:
        ans = input("日本の首都は？('q'でギブアップ)：")
        if ans == "東京":
            print("正解")
            break  # 正解したのでループを抜ける
        if ans == "q":
            print("終了します。")
            print("残念。もう1度考えてみてね。")
            break  # ギブアップしたのでループ終了

if prompt == 10:
    n = int(input("数字を入力してください。"))
    match n:
        case 1:
            print("one")
        case 2:
            print("two")
        case 3:
            print("three")
        case _:
            print("many")

if prompt == 11:
    n = int(input("数値を入力してください。："))
    match n:
        case 1 | 6 | 8 | 10:
            s = "pon"
        case 3:
            s = "pon"
        case _:
            s = "pon"
    print(s)

if prompt == 12:
    ans = input("続けますか？(yes/no)：")
    match ans:
        case "yes" | "y" | "ok":
            print("続行します。")
        case "no" | "n":
            print("終了します。")
