import sys
from transformers import RobertaForSequenceClassification, RobertaTokenizer, pipeline

# ✅ 학습된 모델 및 토크나이저 로드
model_path = "./codebert_cwe476"
model = RobertaForSequenceClassification.from_pretrained(model_path)
tokenizer = RobertaTokenizer.from_pretrained(model_path)

# ✅ 코드 취약점 탐지 파이프라인 설정
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# ✅ 파일 경로 입력 받기
if len(sys.argv) < 2:
    print("❌ 사용법: python model_inference.py <테스트할 C/C++ 파일>")
    sys.exit(1)

file_path = sys.argv[1]  # 사용자가 입력한 파일명

# ✅ 파일 내용 읽기
try:
    with open(file_path, "r", encoding="utf-8") as f:
        test_code = f.read()
except FileNotFoundError:
    print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
    sys.exit(1)

# ✅ 예측 실행
result = classifier(test_code)
print(f"✅ [{file_path}] 예측 결과: {result}")
