prompt = int(input("数値を入力してください："))

if prompt == 1:
    # 読み込んだ数は正の値か
    s = input("数を入力してください：")
    if s.replace(".", "").isdigit():
        n = float(s)
        if n > 0:
            print("正の値です。")
        elif n == 0:
            print("ゼロです。")
        elif n < 0:
            print("負の値です。")
    else:
        print("数ではありません。")
else:
    pass

if prompt == 2:
    # 全部ifにしてみる
    if n > 0:
        print("正です。")
    if n == 0:
        print("ゼロです。")
    if n < 0:
        print("負です。")
else:
    pass


if prompt == 3:
    # 論理型の値を表示
    a = int(input("整数a："))
    b = int(input("整数b："))
    print("a<b:", a < b)
    print("a<=b:", a <= b)
    print("a>b:", a > b)
    print("a>=b:", a >= b)
    print("a==b:", a == b)
    print("a!=b:", a != b)
    print("False:", False)
    print("True:", True)
    print("true+5:", True + 5)  # 1+5とみなされる
else:
    pass


if prompt == 4:
    # 加算を行う式と値比較を行う式
    no = int(input("noの値："))
    print(f"no+135の型は{type(no + 135)}で値は{no + 135}です。")
    print(f"no>135の型は{type(no > 135)}で値は{no > 135}です。")
else:
    pass


# 整数値の桁数（０／１桁／２桁以上）を判定
if prompt == 5:
    n = int(input("整数値："))
    if n == 0:
        print("nは０桁です。")
    elif 1 <= n <= 9:
        print("nは１桁です。")
    else:
        print("nは２桁以上です。")
else:
    pass


if prompt == 6:
    n = int(input("整数値："))
    if n == 0:
        print("nは０桁です。")
    if 1 <= n <= 9:
        print("nは１桁です。")
    if n >= 10:
        print("nは２桁以上です。")
else:
    pass


if prompt == 7:
    # 読み込んだ整数値が２桁以上かを判別する（その１）
    n = int(input("整数値："))
    if n <= -10 or n >= 10:
        print("nは２桁以上です。")
    else:
        print("nは２桁未満です。")

    # 読み込んだ整数値が２桁以上かを判別する（その２）
    n = int(input("整数値："))
    if not (n <= -10 or n >= 10):
        print("nは２桁未満です。")
    else:
        print("nは２桁以上です。")

    print(f"10>5はTrueだけど、notをつけると：{not 10 > 5}")
else:
    pass


if prompt == 8:
    # aはbで割り切れるか
    a = int(input("整数a："))
    b = int(input("整数b："))
    c = b != 0 and a % b
    print(c, end=" ")
    if c:
        print("aはbで割り切れません。")
    else:
        print("aはbで割り切れます。")
else:
    pass


if prompt == 9:
    # bが0でないときのみaをbで割った商を表示
    a = int(input("整数a："))
    b = int(input("整数b："))
    b == 0 or print("a//b:", a // b)
else:
    pass


if prompt == 10:
    # 読み込んだ月の季節を表示
    month = int(input("季節を求めます。\n何月ですか？："))
    if 3 <= month <= 5:
        print("それは春です。")
    elif 6 <= month <= 8:
        print("これは夏です。")
    elif 9 <= month <= 11:
        print("それは秋です。")
    elif month == 12 or 1 <= month <= 2:
        print("それは冬です。")
    else:
        print("そんな月はありません。")
else:
    pass


if prompt == 11:
    month = int(input("季節を求めます。\n何月ですか？："))
    if month in {3, 4, 5}:
        print("それは春です。")
    elif month in {6, 7, 8}:
        print("それは夏です。")
    elif month in {9, 10, 11}:
        print("それは秋です。")
    elif month in {12, 1, 2}:
        print("それは冬です。")
    else:
        print("そんな月はありません。")
else:
    pass


if prompt == 12:
    # ２値の小さいほうを表示
    a = int(input("整数a"))
    b = int(input("整数b"))
    if a < b:
        min2 = a
    else:
        min2 = b
    print(f"小さいほうの値は{min2}です。")

    print()

    # ２値の小さいほうを表示（その２）
    min2 = a if a < b else b
else:
    pass


if prompt == 13:
    score = int(input("点数を入力してください。"))
    print("合格" if score >= 60 else "不合格")
else:
    pass


if prompt == 14:
    # ２値の差
    a = int(input("整数a:"))
    b = int(input("整数b:"))
    print(f"差は{b - a if a < b else a - b}です。")
else:
    pass


if prompt == 15:
    # 読み込んだ整数値の符号を表示（条件演算子）
    n = int(input("整数値："))
    print(f"その値は{'正' if n > 0 else ('0' if n == 0 else '負')}")
else:
    pass


if prompt == 16:
    score = int(input("点数を入力してください。"))
    grade = "A" if score >= 80 else "B" if score >= 70 else "C"
    if score >= 60:
        print(grade + "評価で合格です．")
    else:
        print("不合格です")
else:
    pass
