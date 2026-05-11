prompt = int(input("数値を入力してプロンプトを選択してください。"))
if prompt == 1:
    t = (0, 1, 4, 9, 16, 25, 36, 49)
    print(type(t))
    print(t[0], t[4])
    print(t[::-1])
    print(16 in t)
    print(16 not in t)

if prompt == 2:

    def get_user_deta():
        return "tanaka", 20, "male"  # タプルを返している

    name, age, gender = get_user_deta()  # タプルをアンパックしている
    print(f"名前:{name}, 年齢:{age}, 性別:{gender}")

if prompt == 3:
    a = [1, 2, 3]
    t = tuple(a)  # タプルに変換
    print(t)
    print(type(t))

if prompt == 4:
    a = (1, 2, 3)
    t = list(a)  # リストに変換
    print(t)
    print(type(t))
