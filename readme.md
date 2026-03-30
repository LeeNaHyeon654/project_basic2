# project_basic2

## 1. 프로젝트 개요

통신사 고객 raw 데이터를 입력받아 이탈 위험 여부를 예측하는 시스템입니다.

- Backend API: 입력 수신, DB 저장, Model API 호출, 결과 반환
- Model API: 전처리, 스케일링, 예측 수행
- MariaDB: 원본 고객 데이터 및 예측 결과 저장

## 2. 시스템 구조

Frontend -> Backend API -> MariaDB
                     \-> Model API

## 3. 디렉토리 구조
## 4. 실행 환경

## 5. 로컬 실행 방법

### 1. 가상환경 활성화
source .venv/bin/activate

### 2. model_api 실행
python -m uvicorn model_api.app.main:app --host 127.0.0.1 --port 8001 --reload --reload-dir model_api --reload-dir model

### 3. backend 실행
python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir backend

## 6. API 명세

### POST /customers/predict
신규 고객 raw 데이터를 받아 customer_id를 자동 생성하고 예측 결과를 반환합니다.

### GET /predictions/high-risk
최신 예측 기준 위험군 고객 목록을 반환합니다.

### GET /health
서버 상태 확인용 엔드포인트입니다.

## 7. DB 초기화 방법
## 8. 배치 예측 실행 방법
## 9. 프론트 연동 방법
## 10. 배포 시 고려사항