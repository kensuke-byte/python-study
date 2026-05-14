prompt = int(input("数値を入力してプロンプトを選択してください。"))
if prompt == 1:
    name = ["tanaka", "suzuki", "yamada"]
    NAME = [n.upper() for n in name]  # 大文字に変換
    print(NAME)
else:
    pass

if prompt == 2:
    NAME = ["TANAKA", "SUZUKI", "YAMADA"]
    name = [n.lower() for n in NAME]  # 小文字に変換
    print(name)
else:
    pass

if prompt == 3:
    name = ["tanaka", "suzuki", "yamada"]
    NAME = list(map(str.upper, name))  # 大文字に変換
    print(NAME)
else:
    pass

if prompt == 4:
    n = [1, 2, 3, 4, 5]
    n1 = [str(x).replace("1", "10") for x in n]  # 置換
    print(n1)
    print(type(n1))
else:
    pass

if prompt == 5:
    phone = "090-1234-5678"
    clean_phone = phone.replace("-", "")
    print(clean_phone)
else:
    pass

if prompt == 6:
    text = "今日は晴れです"
    new_text = text.replace("今日", "明日").replace("晴れ", "雨")
    print(new_text)
else:
    pass
