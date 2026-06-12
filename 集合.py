prompt = int(input("数値を入力してプロンプトを選択してください。"))
if prompt == 1:
    # 集合の作成
    s = {"東京", "神奈川", "千葉", "埼玉"}
    print(s)
    print(type(s))
    print(len(s))
    print("東京" in s)
    print("栃木" in s)
    print("埼玉" not in s)
    print()
    print(s.add("栃木"))
    print(s)
    print(s.add("栃木"))
    print(s)
    print(s.remove("栃木"))
    print(s)
else:
    pass

if prompt == 2:
    # ユーザーIDのリスト（同じ人が何回もアクセスして重複している）
    access_logs = ["user1", "user2", "user1", "3", "user2"]

    # setに変換してダブりを消し、またlistに戻す
    unique_users = list(set(access_logs))

    print(unique_users)  # ['user2', 'user1', '3']
else:
    pass

if prompt == 3:
    allowed_users = {"admin", "manager", "staff"}

    if "guest" in allowed_users:
        print("アクセス許可")
    else:
        print("拒否")
else:
    pass

if prompt == 4:
    team_a = {"田中", "佐藤", "鈴木"}
    team_b = {"佐藤", "鈴木", "高橋"}

    # １．積集合（&）：両方のチームに所属している人（共通部分）
    print(team_a & team_b)

    # ２．和集合（|）：どちらかのチームにいる人全員（合体）
    print(team_a | team_b)

    # ③ 差集合（-）：チームAにだけいて、チームBにはいない人（引き算）
    print(team_a - team_b)  # {'田中'}
else:
    pass

if prompt == 5:
    # 基本の形 {要素の計算 for 要素 in データの塊}

    # 通常の書き方
    squares = set()
    for x in [1, 2, 2, 3]:  # 「2」が重複している
        squares.add(x**2)
    # 結果: {1, 4, 9} （4は1つにまとめられる）
    print(squares)

    # 集合の内包表記
    squares = {x**2 for x in [1, 2, 2, 3]}
    print(squares)
else:
    pass

if prompt == 6:
    words = {"apple", "banana", "APPLE", "BANANA"}

    # 1.すべて小文字にしたリストを作る
    lower_list = [w.lower() for w in words]  # ['apple', 'banana', 'apple', 'banana']
    print(lower_list, "\n")
    # 2.集合に変換してダブりを消す
    unique_words = set(lower_list)  # {'apple', 'banana'}
    print(unique_words)
else:
    pass

if prompt == 7:
    words = ["apple", "banana", "APPLE", "Banana"]

    # 小文字に揃えつつ、ダブりのない集合を1行で作る
    unique_words = set(w.lower() for w in words)
    print(unique_words)
else:
    pass

if prompt == 8:
    # ランダムな数字のリスト（重複あり）
    numbers = [1, 2, 3, 2, 4, 5, 4, 6]

    # 「偶数だけ」を2倍にして、ダブりのない集合を作る
    even_squares = {n * 2 for n in numbers if n % 2 == 0}

    print(even_squares)  # {4, 8, 12}
    """
    偶数は [2, 2, 4, 4, 6]。2倍すると [4, 4, 8, 8, 12]。
    集合なのでダブりが消えて {4, 8, 12} になる。
    """
else:
    pass
