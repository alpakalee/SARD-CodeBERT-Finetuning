from transformers import RobertaForSequenceClassification, Trainer
from datasets import load_from_disk
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import confusion_matrix

# ✅ 전처리된 데이터 로드
dataset = load_from_disk("processed_dataset")

# ✅ 학습된 모델 로드
model = RobertaForSequenceClassification.from_pretrained("./codebert_cwe476")

# ✅ Trainer 설정
trainer = Trainer(model=model)

# ✅ 예측 수행
predictions = trainer.predict(dataset["test"])
y_pred = predictions.predictions.argmax(axis=1)  # 가장 높은 확률을 가진 클래스 선택
y_true = predictions.label_ids  # 실제 정답

# ✅ 정확도 & F1-score 계산
accuracy = accuracy_score(y_true, y_pred)
precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="binary")

# ✅ 혼동 행렬 계산
cm = confusion_matrix(y_true, y_pred)
print(f"📊 Confusion Matrix:\n{cm}")

print(f"✅ 모델 평가 결과:")
print(f"📊 정확도 (Accuracy): {accuracy:.4f}")
print(f"📊 정밀도 (Precision): {precision:.4f}")
print(f"📊 재현율 (Recall): {recall:.4f}")
print(f"📊 F1-score: {f1:.4f}")
