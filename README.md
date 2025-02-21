### ✅ **README.md (CodeBERT CWE-476 취약점 탐지 모델)**  

# 🚀 CodeBERT CWE-476 취약점 탐지 모델

CodeBERT를 활용하여 **CWE-476 (Use After Free) 취약점을 탐지하는 모델**입니다.  
이 프로젝트에서는 **C, C++ 소스 코드에서 취약점을 자동으로 탐지**하기 위해 CodeBERT를 파인튜닝(Fine-Tuning)하였습니다.  

---
```md
 📌 프로젝트 구조
📂 codebert_cwe476/
├── dataset.py               # 데이터 파일(.c, .cpp)을 JSON 형식으로 변환
├── split_dataset.py         # JSON 데이터를 Train / Validation / Test로 분리
├── dataset_preprocessing.py # 데이터셋 토큰화 (Tokenization)
├── model_training.py        # CodeBERT 모델 파인튜닝 (Fine-Tuning)
├── model_evaluation.py      # 학습된 모델 평가
├── model_inference.py       # 새로운 코드 파일에서 취약점 탐지
├── processed_dataset/       # 토큰화된 데이터셋 저장
├── results/                 # 학습된 모델 체크포인트 저장
└── README.md                # 프로젝트 설명
```

---

## 📌 실행 방법
```bash
pip install -r requirements.txt
```
### **1️⃣ 데이터 파일(C, C++ 코드)을 JSON으로 변환**
```bash
python dataset.py
```
- dataset.py 안에 있는 파일 경로 수정해야 합니다.
- `.c`, `.cpp` 소스 코드에서 **함수 단위로 분리하여 JSON 형식으로 저장**합니다.  
- 결과 파일: `cwe476_dataset.json`

---

### **2️⃣ 데이터 분리 (Train / Validation / Test)**
```bash
python split_dataset.py
```
- `cwe476_dataset.json`을 **훈련(Train), 검증(Validation), 테스트(Test) 데이터셋으로 분할**합니다.
- 결과 파일: `train.json`, `validation.json`, `test.json`

---

### **3️⃣ 데이터 토큰화 (Tokenization)**
```bash
python dataset_preprocessing.py
```
- `train.json`, `validation.json`, `test.json`을 **CodeBERT 모델이 학습할 수 있도록 토큰화(Tokenization)** 합니다.
- 토큰화된 데이터는 `processed_dataset/`에 저장됩니다.

---

### **4️⃣ CodeBERT 모델 학습 (Fine-Tuning)**
```bash
python model_training.py
```
- CodeBERT(`microsoft/codebert-base`)를 CWE-476 취약점 탐지 모델로 **파인튜닝(Fine-Tuning)** 합니다.
- 학습된 모델은 `./codebert_cwe476/`에 저장됩니다.

---

### **5️⃣ 학습된 모델 검증 (Evaluation)**
```bash
python model_evaluation.py
```
- `test.json`을 사용하여 **모델의 성능(Accuracy, Precision, Recall, F1-score)을 평가**합니다.
- 혼동 행렬(Confusion Matrix)을 출력하여 **모델이 취약점을 잘 탐지하는지 분석**합니다.

---

### **6️⃣ 실제 파일 테스트 (Inference)**
```bash
python model_inference.py <테스트할 C 파일 경로>
```
- 예제:
```bash
python model_inference.py cwe416_split/CWE416_Use_After_Free_bad.c
```
✅ **예측 결과 예시**
```json
✅ [CWE416_Use_After_Free_bad.c] 예측 결과: [{'label': 'LABEL_1', 'score': 0.9987}]
```
👉 **LABEL_1 (취약한 코드)로 예측됨!**

```bash
python model_inference.py cwe416_split/CWE416_Use_After_Free_good.c
```
✅ **예측 결과 예시**
```json
✅ [CWE416_Use_After_Free_good.c] 예측 결과: [{'label': 'LABEL_0', 'score': 0.9912}]
```
👉 **LABEL_0 (안전한 코드)로 예측됨!**

---

## 📌 기술 스택
- **Python 3.8+**
- **PyTorch**
- **Hugging Face Transformers (CodeBERT)**
- **Datasets (Hugging Face)**
- **Scikit-learn (모델 평가)**
- **Imbalanced-learn (SMOTE 데이터 증강)**

---

## 📌 추가 개선 가능 사항
- **다른 CWE 취약점(CWE-119, CWE-787 등) 탐지 모델 확장**
- **데이터 증강(Data Augmentation) 기법 적용 (SMOTE 외에도 코드 변형 기법 추가)**
- **실제 오픈소스 프로젝트 코드에서 취약점 탐지 테스트**

---

## 🚀 결론
이 프로젝트는 **CodeBERT를 활용하여 CWE-476(Use After Free) 취약점을 자동 탐지하는 모델**입니다.  
단순한 코드 분석을 넘어 **AI 기반 보안 취약점 탐지 모델을 연구하는 데 유용한 프레임워크**가 될 수 있습니다.  
🚀 **보안 연구, AI 기반 취약점 탐지, CodeBERT 활용 프로젝트를 위한 최고의 출발점!**  

---

## 📌 GitHub 업로드 방법
### **Git 설정**
```bash
git init
git remote add origin https://github.com/USERNAME/codebert_cwe476.git
git branch -M main
git add .
git commit -m "🚀 Initial commit: CodeBERT CWE-476 취약점 탐지 모델"
git push -u origin main
```
