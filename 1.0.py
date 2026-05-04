# 数値リテラル
print(0b10)
print(0o10)
print(10)
print(0x10)
print(3.14e-7)
print(34_23_36)
# 文字列リテラル
print("kensuke")
print("小林")
print("k" + "e" + "n" + "s" + "u" + "k" + "e")
print("k" * 7)
print("小林" + "です。")
print(2 * "小林" * 3)
print("string")
print("string")
print("""string""")
print("""string""")
print("それはABCです。")
print(
    "文字列\"ABC\"を構成するのは'A'と'B'と'C'です"
    "とても長い文字列を表示することもできます。"
)
print("文字列\"ABC\"を構成するのは'A'と'B'と'C'です。")
print("""途中で
改行
できます。""")
# エスケープシーケンス
print("it's a pen")
print("小林です。\nこんにちは。")
# 隣接した文字列リテラル
print("hellowworld")
# 原文字列リテラル
print(r"c:\name\kensuke")
print(r" ")

# 変数
print("ここから変数です。")
x = 17
y = 52
z = x + y
print(x)
print(y)
print(z)
print(x, y, z)
x = 17
print(x)
x = 3.14
print(x)
x = "ABC "
print(x)

print("")
x = 17
print(type(x))
x = 3.14
print(type(x))
x = "ABC"
print(type(x))

print("")
print(type(5))
print(type(3.14))
print(type("ABC"))

print("")
# 式と文
x = 3
print(x + 14)
x = 0
print(type(x + 14))

print("")
# 代入文
x = y = 1
print(x)
print(y)
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
x = 6
y = 2
x, y = y + 2, x + 3
print(x)
print(y)
x = 1
print(x)
print(
    "これは、すごく、すごく、すごく、すごく、すごく、\
長い文章を表示するためのコードです。"
)
