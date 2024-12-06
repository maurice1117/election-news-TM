import pandas as pd
import re
from transformers import pipeline


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

data['text_length'] = data['cleaned_text'].apply(len)
print(data['text_length'].describe())

"""
# 加載 Hugging Face 的情感分析管道
sentiment_pipeline = pipeline("sentiment-analysis", model="allenai/longformer-base-4096", framework="tf")# 使用 TensorFlow

data['sentiment'] = data['cleaned_text'].apply(lambda x: sentiment_pipeline(x)[0]['label'])


print(data['sentiment'].value_counts(normalize=True))  # 顯示情感比例
"""