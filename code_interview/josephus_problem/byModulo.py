def josephus_problem(n):
    # 初始化一個從1到n的列表，表示n個人
    people = list(range(1, n + 1))

    # 報數的起始位置
    index = 0

    # 當還有多於一個人時，繼續報數
    while len(people) > 1:
        # 每次跳過8個人，報到3的人出圈（因為列表索引從0開始，所以用 index + 2）
        index = (index + 2) % len(people)
        # 移除報到9的那個人
        people.pop(index)

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
