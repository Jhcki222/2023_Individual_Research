import numpy as np
import pandas as pd
from konlpy.tag import Okt

df = pd.read_excel('test1.xlsx')
df.head(3)

articles = df['Comments'].tolist()
print(len(articles))  # 30

articles = ' '.join(articles)
articles = articles[:10000]
print(articles)



tokenizer = Okt()
raw_pos_tagged = tokenizer.pos(articles, norm=True, stem=True) # POS Tagging
print(raw_pos_tagged)

del_list = ['를', '이', '은', '는', '있다', '하다', '에']  
# 불용어 제거
word_cleaned = []
for word in raw_pos_tagged:
    if not word[1] in ["Josa", "Eomi", "Punctuation", "Foreign"]: # Foreign == ”, “ 와 같이 제외되어야할 항목들
        if (len(word[0]) != 1) & (word[0] not in del_list): # 한 글자로 이뤄진 단어들을 제외 & 원치 않는 단어들을 제외, 대신 "안, 못"같은 것까지 같이 지워져서 긍정,부정을 파악해야 되는경우는 제외하지 않는다.
            word_cleaned.append(word[0])
        
print(word_cleaned)