# 例外
try:
    prompt = int(input("数値を入力してプロンプトを選択してください。"))
except ValueError:
    print("エラーが発生しました。")
    exit()


# 例外の捕捉

if prompt == 1:
    try:
        print(f"{2 / 0}")
    except ZeroDivisionError:
        print("エラーが発生しました。")
        exit()
else:
    pass

if prompt == 2:
    try:
        2.0**1024
    except OverflowError as e:
        print("オーバーフロー:", e)

if prompt == 3:
    try:
        # 存在しないキーを指定してみる
        user = {"name": "田中"}
        print(user["age"])
    # エラー内容を「e」という変数に捕まえる（名前はなんでもOK）
    except KeyError as e:
        print(f"エラーが発生しました。原因となったキー: {e}")
else:
    pass


# 例外の捕捉には「具体的なエラーから順番に書く」という鉄則があります。
if prompt == 4:
    try:
        # 何が起きるか分からない危険な処理
        result = 10 / int(input("数字を入力してください。"))

    except ZeroDivisionError:
        # 0で割ったとき
        print("ゼロでは割れません")

    except Exception as e:
        # それ以外のエラー
        print(f"予期せぬエラーが発生しました: {type(e).__name__} - {e}")
else:
    pass


if prompt == 5:
    try:
        # 設定ファイルを読み込んで数字に変換する
        with open("config.txt", "r") as f:
            num = int(f.read())

    except (FileNotFoundError, ValueError) as e:
        # ファイルがない、または中身が数字じゃない、どちらのエラーもここでキャッチ！
        print(f"設定ファイルの読み込みに失敗しました。デフォルト値を使用します。({e})")
        num = 10
else:
    pass


# 例外の送出

if prompt == 6:
    # raise文を用いると、自分で実装したコードの中から例外を送出できる
    def timestamp(hour, minute, second):
        if hour < 0 or hour <= 24:
            raise ValueError("引数hourは0 <= hour < 24を満たす必要があります")
        if minute < 0 or 60 <= minute:
            raise ValueError("引数minuteは0 <= minute < 60を満たす必要があります")
        if second < 0 or 60 <= second:
            raise ValueError("引数secondは0 <= second < 60を満たす必要があります")
        return hour * 3600 + minute * 60 + second

    timestamp(2, 43, 70)

    # 関数の呼び出し側にtry文を埋め込み、例外を捕捉することも可能である。
    try:
        timestamp(48, 0, 0)
    except ValueError as e:
        print("例外:", type(e), e)
else:
    pass

if prompt == 7:
    # 例外クラスを自分で定義することもできる。
    # ユーザ定義の例外クラスはExceptionを継承する必要がある。
    class TimestampError(Exception):
        pass

    def timestamp(hour, minute, second):
        if hour < 0 or 24 <= hour:
            raise TimestampError("引数hourは0 <= hour < 24を満たす必要があります")
        if minute < 0 or 60 <= minute:
            raise TimestampError("引数minuteは0 <= minute < 60を満たす必要があります")
        if second < 0 or 60 <= second:
            raise TimestampError("引数secondは0 <= second < 60を満たす必要があります")
        return hour * 3600 + minute * 60 + second

    timestamp(1, 95, 22)
else:
    pass

if prompt == 8:
    # デバッグ目的であればassert文を使い、引数の値をチェック（テスト）して、
    # 違反していたらAssertionErrorを送出することもできる。
    def timestamp(hour, minute, second):
        assert 0 <= hour < 24, "引数hourは0 <= hour < 24を満たす必要があります"
        assert 0 <= minute < 60, "引数minuteは0 <= minute < 60を満たす必要があります"
        assert 0 <= second < 60, "引数secondは0 <= second < 60を満たす必要があります"
        return hour * 3600 + minute * 60 + second

    timestamp(2, 43, 70)

if prompt == 9:

    def damage_player(player_name, damage):
        if damage < 0:
            raise ValueError("引数damageは0以上である必要があります")
        print(f"{player_name}は{damage}ダメージを受けました。")

    damage_player("プレイヤー1", -10)
else:
    pass
