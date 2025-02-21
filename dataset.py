# 초기 SARD 에서 json으로 출력
import os
import json
import re

# CWE-476 데이터셋 폴더 경로 및 출력 파일 경로
DATASET_PATH = r"C:\Users\user\Desktop\121"
OUTPUT_JSON = "cwe121_dataset.json"

# 데이터셋 저장 리스트
dataset = []

# 정규식을 이용해 C 및 C++ 함수 단위로 코드 추출 (C 함수 정의 패턴)
FUNCTION_PATTERN = re.compile(r"\b(?:void|static void)\s+(CWE121__\w+|good\w*|bad\w*)\s*\([\s\S]*?\{", re.MULTILINE)

# CWE-476 폴더에서 .c, .cpp 파일 추출
if os.path.exists(DATASET_PATH):
    for root, _, files in os.walk(DATASET_PATH):
        for file in files:
            if file.endswith((".c", ".cpp")):  # 헤더 파일 제외
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                    # 함수 단위로 코드 분리
                    matches = FUNCTION_PATTERN.finditer(code)
                    functions = {}

                    for match in matches:
                        function_name = match.group(1)  # 함수 이름 추출
                        start_idx = match.start()  # 함수 시작 위치

                        # 함수 끝(괄호 닫힘) 찾기
                        brace_count = 0
                        end_idx = start_idx
                        in_function = False
                        for i in range(start_idx, len(code)):
                            if code[i] == "{":
                                brace_count += 1
                                in_function = True
                            elif code[i] == "}":
                                brace_count -= 1
                                if brace_count == 0 and in_function:
                                    end_idx = i + 1
                                    break

                        function_code = code[start_idx:end_idx]  # 함수 코드 추출

                        # good* 함수명을 CWE~~~_good* 형태로 변경
                        if function_name.startswith("good"):
                            base_name = file.replace(".c", "").replace(".cpp", "")  # 파일명에서 확장자 제거
                            function_name = f"{base_name}_{function_name}"

                        functions[function_name] = function_code.strip()  # 저장

                    # 저장된 함수에서 각각 JSON 항목으로 변환
                    for function_name, function_code in functions.items():
                        label = 1 if "bad" in function_name.lower() else 0  # bad가 포함된 함수는 취약코드
                        dataset.append({
                            "filename": file,
                            "code": function_code.strip(),
                            "target": label
                        })

    # JSON 저장
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4)

    print(f"✅ CWE-476 데이터셋이 함수 단위로 분리되어 {OUTPUT_JSON}로 저장됨!")
else:
    print(f"❌ 데이터셋 폴더 {DATASET_PATH}가 존재하지 않습니다. 파일 경로를 확인하세요.")
