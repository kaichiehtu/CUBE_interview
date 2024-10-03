def correct_scores(wrong_scores):
    correct_scores = []
    
    for score in wrong_scores:
        # 取出十位數和個位數，然後對調
        tens = score // 10
        ones = score % 10
        corrected_score = ones * 10 + tens
        
        correct_scores.append(corrected_score)
    
    return correct_scores

# 錯誤的成績列表
wrong_scores = [35, 46, 57, 91, 29]

# 修正後的成績
fixed_scores = correct_scores(wrong_scores)
print(fixed_scores)  # 輸出: [53, 64, 75, 19, 92]
