def count_letters_and_digits(text):
    # 將所有字母和數字轉換為小寫
    text = text.lower()
    counts = {}

    # 遍歷字串中的每個字符
    for char in text:
        if char.isalnum():  # 統計字母和數字
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

    return counts

# 需要計算的文字
text = "Hello welcome to Cathay 60th year anniversary"

# 計算每個字母和數字出現的次數
counts = count_letters_and_digits(text)

# 輸出結果，依照字母和數字的順序，且只顯示出現次數大於零的字符
for char in sorted(counts.keys()):  # 對鍵進行排序
    if counts[char] > 0:  # 只顯示出現次數大於零的字符
        print(f"{char}: {counts[char]}")