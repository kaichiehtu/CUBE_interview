class Node:
    """節點類，用於圓形鏈表"""
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    """圓形鏈表類"""
    def __init__(self):
        self.head = None

    def append(self, value):
        """在圓形鏈表尾部添加節點"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # 自我連結
        else:
            current = self.head
            while current.next != self.head:  # 找到尾部節點
                current = current.next
            current.next = new_node
            new_node.next = self.head  # 新節點連回頭部

    def remove(self, value):
        """從圓形鏈表中移除指定值的節點"""
        current = self.head
        prev = None

        # 如果只有一個節點
        if current and current.value == value:
            if current.next == self.head:
                self.head = None
            else:
                # 找到尾部節點
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        # 迴圈尋找節點
        while True:
            if current.value == value:
                if prev:
                    prev.next = current.next
                break
            prev = current
            current = current.next
            if current == self.head:  # 迴圈回到起點
                break

def josephus_problem(n):
    """約瑟夫問題實現"""
    circle = CircularLinkedList()
    for i in range(1, n + 1):
        circle.append(i)

    current = circle.head

    # 繼續操作，直到只剩下最後一個人
    while current and current.next != current:  # 當圓形鏈表中有超過一個節點時
        # 跳過兩個人，然後刪除第三個人
        current = current.next.next  # 移動到第三個人
        circle.remove(current.value)  # 刪除當前人

        # 移動到下個人
        current = current.next

    # 返回最後剩下的人的順位
    return current.value

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