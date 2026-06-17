prompt = int(input("数値を入力してプロンプトを選択してください。"))


# インスタンス化
if prompt == 1:

    class Character:
        def __init__(self, name, job):
            self.name = name
            self.job = job

    # ーーー 👇 ここが「インスタンス化」の瞬間！ ーーー
    player1 = Character("プレイヤー1", "ゲームクラス")
    player2 = Character("プレイヤー2", "ゲームクラス")
    print(player1.name)
    print(player2.name)
    print(player1.job)
    print(player2.job)
else:
    pass

if prompt == 2:
    # クラスをインスタンス化してPointオブジェクトを作成する。
    class Point:
        """
        class: 自分だけのオリジナルなデータ型（仕組み）」を作成するときに使用する。
        """

        # 作成されたオブジェクトを引数として__init__関数が呼び出される。
        def __init__(self):
            """
            init: nitialization（初期化） の略で、オブジェクトを初期化する。
            """
            # .演算子を適用することで、メンバ変数xとyを0.に初期化している。
            self.x = 0.0
            self.y = 0.0

    p = Point()
    print(type(p))
    print(p)
    print(p.x)
    print(p.y)
    print()
    p.x = 10
    p.y = 20
    print(p.x)
    print(p.y)
else:
    pass

if prompt == 3:
    # __init__関数で引数を受け取り、メンバ変数を初期化することも可能。
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

    p = Point(10, 20)
    print(p.x)
    print(p.y)
else:
    pass

# メソッド
"""
インスタンスのメンバ変数に対する操作などをメンバ関数（メソッド）として記述できる。
メンバ関数の第１引数としてインスタンスが渡されるため、
第１引数をselfという変数名にするのが慣例。
"""
if prompt == 4:

    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def set(self, x, y):
            self.x = x
            self.y = y

        def transpose(self):
            self.x, self.y = self.y, self.x

        def hamming(self):
            return self.x + self.y

        def dot(self, other):
            return self.x * other.x + self.y * other.y

    p = Point()
    print(p.x)
    print(p.y)
    print()
    p.set(10, 20)
    print(p.x)
    print(p.y)
    print()
    Point.set(p, 20, 30)
    print(p.x)
    print(p.y)
    print()
    p.transpose()
    print(p.x)
    print(p.y)
    print()
    print(p.hamming())
    print()
    p = Point(2, 3)
    q = Point(5, 4)
    print(p.dot(q))
    print()
    print(dir(p))
else:
    pass


"""
プログラミングの世界では、データ（名前や数値など）を「属性」と呼ぶのに対し、
そのデータを使って何かをする「動き・処理」のことをメソッドと呼びます。

関数（Function）：
どこにでも属していない、独立した機能。単体で呼び出せる。
例：print(), len()

メソッド（Method）：
クラスの中に書かれていて、そのクラスから作ったインスタンス（実物）からしか呼び出せない機能。
例：リストの .append(), 文字列の .upper()
"""


# クラスの中で def を使って定義しますが、
# 最大の特徴は「第1引数に必ず self（自分自身）を書く」というルールです。
if prompt == 5:

    class dog:
        def __init__(self, name):
            self.name = name

        # ーーー 👇 これがメソッド！ ーーー
        def bark(self):
            # self を使うことで、自分の「名前」にアクセスできる
            print(f"{self.name} :ワンワン")

        def eat(self, food):
            # 引数（food）を追加して、データを受け取ることもできる。
            print(f"{self.name} は{food}を食べた。")

    # インスタンス化（ポチという犬を作る）
    pochi = dog("ポチ")

    # オブジェクト.動詞()
    # メソッドを呼び出す
    pochi.bark()
    pochi.eat("骨")
else:
    pass


# 継承
"""
あるクラスをベースとしてメンバ変数・関数を追加し、新しいクラスを定義することを継承と呼ぶ。
"""
if prompt == 6:
    # 1. 親クラス（ベースとなる普通のキャラクター）
    class Character:
        def __init__(self, name, hp):
            self.name = name
            self.hp = hp

        def walk(self):
            print(f"{self.name}はトコトコ歩いた。")

    # 2. 子クラス（Characterを引き継いだ「魔法使い」）
    class Mage(Character):  # カッコの中に親クラスを書く！
        """
        親の機能はすべて自動で引き継がれるので、
        ここには「魔法使い独自の機能」だけを書けばOK
        """

        def cast_magic(self):
            print(f"{self.name}は魔法の呪文を唱えた！")

    # 魔法使いのインスタンスを作る
    wizard = Mage("レフィ", 60)

    # 親から引き継いだメソッドが使える！
    wizard.walk()  # レフィはトコトコ歩いた。

    # 自分独自のメソッドも、もちろん使える！
    wizard.cast_magic()  # レフィは魔法の呪文を唱えた！

    # 親の機能を上書きする「オーバーライド」
    class Hero(Character):
        # 親と同じ名前のメソッドを書くと、上書き（オーバーライド）される
        def walk(self):
            print(f"{self.name}は素早く歩いた。")

    brave = Hero("シン", 100)
    brave.walk()  # シンは素早く歩いた。（親のトコトコは無視される）
else:
    pass


# 特殊メソッド
"""
自分で定義したクラスのオブジェクトに対して、
+演算子の動作やstr関数を呼び出したときの動作を特殊メソッドに記述できる。
"""
if prompt == 7:

    class Point:
        """Two-demensional vector"""

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            """str(p)"""
            return f"({self.x}, {self.y})"

        def __repr__(self):
            """repr(p)"""
            return f"Point({self.x}, {self.y})"

        def __add__(self, other):
            """self + other"""
            return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            """self - other"""
            return Point(self.x - other.x, self.y - other.y)

        def __mul__(self, other):
            """self * other"""
            return Point(self.x * other.x, self.y * other.y)

        def __rmul__(self, other):
            """other * self"""
            return Point(self.x * other, self.y * other)

        def __truediv__(self, other):
            """self / other"""
            return Point(self.x / other.x, self.y / other.y)

        def __floordiv__(self, other):
            """self // other"""
            return Point(self.x // other.x, self.y // other.y)

        def __eq__(self, other):
            """self == other"""
            return self.x == other.x and self.y == other.y

        def __ne__(self, other):
            """self != other"""
            return not self.__eq__(other)

        def __lt__(self, other):
            """self < other"""
            return self.x < other.x and self.y < other.y

        def __le__(self, other):
            """self <= other"""
            return self.__lt__(other) or self.__eq__(other)

        def __gt__(self, other):
            """self > other"""
            return self.x > other.x and self.y > other.y

        def __ge__(self, other):
            """self >= other"""
            return self.__gt__(other) or self.__eq__(other)

        def set(self, x, y):
            self.x = x
            self.y = y

        def transpose(self):
            self.x, self.y = self.y, self.x

        def hamming(self):
            return self.x + self.y

        def dot(self, other):
            return self.x * other.x + self.y * other.y

    # Pointクラスのインスタンスp1とp2を作成
    p1 = Point(2, 3)
    p2 = Point(5, 6)

    # +演算子を使うと、__add__が呼び出される。
    print(p1 + p2)
    # -演算子を使うと、__sub__が呼び出される。
    print(p1 - p2)
    # *演算子を使うと、__mul__が呼び出される。
    print(p1 * p2)
    print(3 * p1)
    # /演算子を使うと、__truediv__が呼び出される。
    print(p1 / p2)
    # ==演算子を使うと、__eq__が呼び出される。
    print(p1 == p2)
    #!=演算子を使うと、__ne__が呼び出される。
    print(p1 != p2)
    # <演算子を使うと、__lt__が呼び出される。
    print(p1 < p2)
    # <=演算子を使うと、__le__が呼び出される。
    print(p1 <= p2)
    # >演算子を使うと、__gt__が呼び出される。
    print(p1 > p2)
    # >=演算子を使うと、__ge__が呼び出される。
    print(p1 >= p2)
else:
    pass
