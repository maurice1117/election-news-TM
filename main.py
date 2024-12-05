import pandas as pd
import re

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # 移除 URL
    text = re.sub(r"@\w+", "", text)    # 移除提及
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # 移除非字母字符
    text = text.lower().strip()  # 小寫化並去除多餘空格
    return text

# 讀取csv檔
file_path = './src/top_election_posts_2024.csv'
data = pd.read_csv(file_path, encoding='latin1')

# 處理缺失值
data = data.dropna(subset=['text'])

# 清理資料
data['cleaned_text'] = data['text'].apply(clean_text)

# 刪除空白或過短的行
data = data[data['cleaned_text'].str.strip().str.len() > 5]

