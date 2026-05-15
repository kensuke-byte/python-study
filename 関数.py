prompt = int(input("数値を入力してください。："))
if prompt == 1:

    def w(n):
        for i in range(n):
            print("w", end="")

    w(3)
else:
    pass


if prompt == 2:

    def w(n, c):
        for i in range(n):
            print(c, end="")

    w(3, "負")
else:
    pass


if prompt == 3:

    def check_odd_even(number):
        if number % 2 == 0:
            return "偶数"
        else:
            return "奇数"

    result = check_odd_even(2)
    print(f"この数字は{result}です。")
else:
    pass


if prompt == 4:

    def draw_line(length, symbol):
        print(length * symbol)

    draw_line(10, "_")
    draw_line(4, "-")
    draw_line(4, "<>")
else:
    pass


if prompt == 5:

    def safe_divide(a, b):
        if b == 0:
            return "0で割ることはできません。"
        return a / b

    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
else:
    pass


if prompt == 6:

    def calculate_tax(price):
        total = price * 1.1  # 10%税金を計算
        return total  # 計算結果を渡す

    pay_amount = calculate_tax(1000)
    print(f"お支払いは{pay_amount}です。")
else:
    pass


if prompt == 7:
    # 戻り値１：税込み価格を出す
    def get_tax_price(price):
        """
        税抜き価格から10%の税込み価格を計算する。
        引数：price(int)：商品の本体価格
        int：小数点以下を切り捨てた税込み価格
        """
        return int(price * 1.1)

    # 戻り値２：ポイントを出す（１００円で１ポイント）
    def get_points(amount):
        """
        支払金額に応じたポイントを計算する（100円で1ポイント）
        引数：amount(int)：最終的な支払金額の戻り値
        戻り値：int：付与されるポイント
        """
        return amount // 100

    # ーーーメインの処理ーーー
    target_price = 3000

    # バトンタッチ
    final_price = get_tax_price(target_price)  # 3300が返る
    points = get_points(final_price)  # 3300をもとに33が返る

    print(f"代金：{final_price}円、獲得ポイント：{points}pt")
else:
    pass


if prompt == 8:

    def fg(x):
        return x**2 - 2, 2 * x

    fx, gx = fg(0)
    print(fx, gx)
else:
    pass


if prompt == 9:
    a = 2025
    print("This year is", a)
    print(f"This year is {a}")
    print("This year is" + str(a))
else:
    pass


if prompt == 10:

    def say_hello(name):  # nameという材料をもらう
        messege = f"こんにちは{name}さん"
        return messege  # 作ったメッセージを返す

    # 使うとき
    result = say_hello("田中")
    print(result)
else:
    pass


if prompt == 11:

    def repeat_star(count):
        """星を指定された回数だけ並べる関数"""
        for i in range(count):
            print("@", end="")

    # 使うとき
    repeat_star(5)
else:
    pass


if prompt == 12:

    def tasu(a, b):
        return a + b

    # 関数を「calc」という名前の変数に代入
    calc = tasu
    print(calc(10, 5))
else:
    pass

if prompt == 13:

    def double(n):
        return n * 2

    def apply_function(func, value):
        """受け取った関数(func)に、値(value)を放り込む関数"""
        return func(value)

    # doubleという処理のルールをあげる
    result = apply_function(double, 10)
    print(result)
else:
    pass


if prompt == 14:

    def decimal(*args):
        v = 0
        for arg in args:
            v *= 10
            v += arg
        return v

    # 試し
    print(decimal(3, 2, 4))
else:
    pass


if prompt == 15:

    def sum_all(*args):
        # argsは「タプル（詰め合わせセット）」として届く
        return sum(args)

    # 試し
    print(sum_all(1, 2))  # 3
    print(sum_all(1, 2, 3, 4, 5))  # 15
else:
    pass


if prompt == 16:

    def print_info(**kwargs):
        """
        kwargs:キーワード付き可変長引数
        kwargsの中身は｛'名前'：'田中', '年齢'：25｝
        という辞書になっている
        """
        print(kwargs)

    # 呼び出し方は「変数=値」をカンマでつなぐ
    print_info(名前="田中", 年齢=25, 住所="東京")
else:
    pass
