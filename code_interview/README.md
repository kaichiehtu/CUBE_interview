# 字母與數字計數程式 charcounter.py

## 描述
這段程式碼實現了計算輸入字串中每個字母和數字出現次數的功能。所有字母會轉換為小寫，並將結果依照字母和數字的順序進行排序。此程式可以用來分析文本中的字母和數字分佈情況。

## 功能
- 計算字串中每個字母和數字的出現次數。
- 將所有字母轉換為小寫，以便統計時不區分大小寫。
- 最終結果會依照字母和數字的順序進行排序，並僅顯示出現次數大於零的字符。

## 使用方法

### 1. 安裝與執行
無需安裝任何額外的包，直接使用 Python 3.x 環境運行即可。

### 2. 執行程式
將以下程式碼複製到您的 Python 編輯器或 IDE 中，然後運行：

`python
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
`
# 需要計算的文字
text = "Hello welcome to Cathay 60th year anniversary"

# 計算每個字母和數字出現的次數
counts = count_letters_and_digits(text)

# 輸出結果，依照字母和數字的順序，且只顯示出現次數大於零的字符
for char in sorted(counts.keys()):  # 對鍵進行排序
    if counts[char] > 0:  # 只顯示出現次數大於零的字符
        print(f"{char}: {counts[char]}")

### 時間複雜度     
這段程式的時間複雜度為 O(n)，其中 n 是輸入字串的長度。程式遍歷字串中的每個字符一次，並對每個字母和數字進行了常數時間的計算和儲存操作。接下來，對所有出現的字符進行排序操作，這部分的時間複雜度為 O(k log k)，其中 k 是出現的字符數。然而，因為 k 通常比 n 小，因此整體的時間複雜度仍可視為 O(n)。


# 成績修正程式 switchElements.py

## 描述
這段程式碼用於修正一組錯誤的成績。由於老師在輸入成績時將十位數和個位數看反，因此需要對調每個成績的十位數和個位數，以得到正確的成績。

## 功能
- 接收一個包含錯誤成績的列表。
- 對於每個成績，將其十位數和個位數進行對調。
- 返回修正後的成績列表。

## 使用方法

### 1. 安裝與執行
無需安裝任何額外的包，直接使用 Python 3.x 環境運行即可。

### 2. 執行程式
將以下程式碼複製到您的 Python 編輯器或 IDE 中，然後運行：

`python
def correct_scores(wrong_scores):
    correct_scores = []
    
    for score in wrong_scores:
        # 取出十位數和個位數，然後對調
        tens = score // 10
        ones = score % 10
        corrected_score = ones * 10 + tens
        
        correct_scores.append(corrected_score)
    
    return correct_scores
`
# 錯誤的成績列表
wrong_scores = [35, 46, 57, 91, 29]

# 修正後的成績
fixed_scores = correct_scores(wrong_scores)
print(fixed_scores)  # 輸出: [53, 64, 75, 19, 92]

# 時間複雜度
這段程式的時間複雜度為 O(n)，其中 n 是錯誤成績列表的長度。程式會遍歷整個列表中的每個成績，並對每個成績進行常數時間的計算和修正操作。因此，隨著輸入成績數量的增加，執行時間會線性增長。