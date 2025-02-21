# json 토큰화
import json
from datasets import load_dataset
from transformers import RobertaTokenizer

# ✅ JSON 데이터셋 경로
train_dataset_path = "train.json"
validation_dataset_path = "validation.json"
test_dataset_path = "test.json"

# ✅ CodeBERT Tokenizer 로드
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")

def tokenize_function(examples):
    """ CodeBERT가 학습할 수 있도록 코드 데이터(Tokenization) """
    tokenized = tokenizer(examples["code"], padding="max_length", truncation=True, max_length=512)
    tokenized["labels"] = examples["target"]  # ✅ labels 추가 (정답값 지정)
    return tokenized

# ✅ 데이터 로드 및 토큰화 적용 (Validation 데이터 추가)
dataset = load_dataset("json", data_files={
    "train": train_dataset_path,
    "validation": validation_dataset_path,  # ✅ Validation 추가
    "test": test_dataset_path
})
# tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["filename", "code", "function_name", "target"])
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["filename", "code", "target"])

# ✅ 변환된 데이터셋 저장
tokenized_datasets.save_to_disk("processed_dataset")

print("✅ 데이터 전처리 및 토큰화 완료! 저장 위치: processed_dataset/")
