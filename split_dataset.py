# json을 훈련, 테스트 분리
import json
import random

# JSON 데이터 파일 경로
INPUT_JSON = "cwe121_dataset_filtered.json"
TRAIN_JSON = "train.json"
VALIDATION_JSON = "validation.json"
TEST_JSON = "test.json"

# 데이터 로드
with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

# 데이터 랜덤 셔플
random.shuffle(data)

# 데이터셋 분할 (80% Train, 20% Test) 0.8
split_ratio = 0.2
split_index = int(len(data) * split_ratio)

train_data = data[:split_index]
test_data = data[split_index:]

val_split_ratio = 0.15
val_split_index = int(len(train_data)*val_split_ratio)

validation_data = train_data[:val_split_index]
train_data = train_data[val_split_index:]

# 분할된 데이터 저장
with open(TRAIN_JSON, "w", encoding="utf-8") as f:
    json.dump(train_data, f, indent=4)

with open(TEST_JSON, "w", encoding="utf-8") as f:
    json.dump(test_data, f, indent=4)
    
with open(VALIDATION_JSON, "w", encoding="utf-8") as f:
    json.dump(validation_data, f, indent=4)

print(f"✅ 데이터셋이 분할되었습니다! Train: {len(train_data)}개, Validation: {len(validation_data)}개, Test: {len(test_data)}개")