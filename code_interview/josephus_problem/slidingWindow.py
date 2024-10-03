def josephus_problem(n):
    # 創建一個列表，表示n個人
    people = list(range(1, n + 1))

    # 繼續操作，直到只剩下最後一個人
    while len(people) > 1:
        # 使用for迴圈進行兩次移動
        for _ in range(2):  # 執行兩次
            people.append(people.pop(0))  # 將第一個人移動到最後

        # 刪除現在的第一個人（報到3的人）
        people.pop(0)  # 刪除第一個人

    # 返回最後剩下的人的順位
    return people[0]

# 輸入人數 n
n = int(input("請輸入參與人數 (0-100): "))

# 檢查 n 是否在有效範圍內
if 0 <= n <= 100:
    # 計算最後留下的同事位置
    result = josephus_problem(n)
    # 輸出結果
    print(f"最後留下的是第 {result} 位同事")
else:
    print("請輸入一個有效的範圍 (0-100)")
