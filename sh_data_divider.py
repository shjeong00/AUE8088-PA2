import numpy as np
from sklearn.model_selection import train_test_split
# 데이터를 불러옵니다.
with open('train_finale.txt', 'r') as f:
#with open('train-all-04.txt', 'r') as f:
    data = f.readlines()
    
# 데이터 섞기
np.random.shuffle(data)
# 데이터를 훈련 세트와 검증 세트로 나sna
train_data, validation_data = train_test_split(data, test_size=0.2, random_state=42)
# 훈련 세트를 파일로 저장
with open('train_0.8_d.txt', 'w') as f:
    for item in train_data:
        f.write("%s" % item)
# 검증 세트를 파일로 저장
with open('validation_0.2_d.txt', 'w') as f:
    for item in validation_data:
        f.write("%s" % item)
