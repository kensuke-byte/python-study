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
