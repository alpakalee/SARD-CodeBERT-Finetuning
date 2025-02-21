import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification, TrainingArguments, Trainer
from datasets import load_from_disk
from transformers import EarlyStoppingCallback

# ✅ GPU 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ✅ 전처리된 데이터 로드
dataset = load_from_disk("processed_dataset")

# ✅ CodeBERT 모델 로드 및 GPU로 이동
model = RobertaForSequenceClassification.from_pretrained("microsoft/codebert-base", num_labels=2).to(device)

# ✅ Dropout 비율 조정 (기본값: 0.1 → 증가)
model.config.hidden_dropout_prob = 0.5  # 기본값: 0.1 → 0.3으로 증가
model.config.attention_probs_dropout_prob = 0.5  # Attention Layer에서도 Dropout 적용

# ✅ 학습 설정
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.2,
    logging_dir="./logs",
    fp16=True,  # ✅ GPU 성능 최적화 (Mixed Precision)
    load_best_model_at_end=True,  # ✅ Early Stopping 적용
    remove_unused_columns=False
)

# ✅ Trainer 설정
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],  # ✅ Validation 데이터 추가
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],  # ✅ 2 epoch 동안 개선 없으면 중단
)

# ✅ 학습 시작
trainer.train()

# ✅ 모델 저장
model.save_pretrained("./codebert_cwe476")
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
tokenizer.save_pretrained("./codebert_cwe476")

print("✅ 모델 학습 완료 및 저장됨!")
