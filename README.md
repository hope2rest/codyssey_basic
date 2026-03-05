# codyssey_basic

Python 기초 미션(터미널 퀴즈 게임) 완료 후 치르는 3문항 시험입니다.
pytest 기반 자동 채점으로, 각 문항 100점 총 300점입니다.

## 구조

```
sample/
├── q1/  CSV 파싱 및 채점 (함수)         4 tests, 100점
├── q2/  퀴즈 클래스 구현 (OOP)          4 tests, 100점
└── q3/  Git 시뮬레이터 (클래스 + JSON)  4 tests, 100점
```

각 폴더 구성:

| 파일 | 용도 |
|------|------|
| `q{N}_*.py` | 학생 제출용 skeleton |
| `q{N}_*_solution.py` | 정답지 |
| `test_q{N}_*.py` | pytest 채점 테스트 |
| `q{N}_*.md` | 문제 설명 |
| `data/` | 데이터 파일 |

## Q1 → Q2 → Q3 연결

| 문항 | 주제 | 이전 문항과의 연결 |
|------|------|--------------------|
| Q1 | CSV 파싱, 리스트/딕셔너리 | - |
| Q2 | Q1 로직을 클래스로 리팩토링 | 동일 CSV, 동일 답안, 동일 결과 |
| Q3 | Git add/commit/push/pull 시뮬레이터 | Q2 결과를 JSON으로 로드 |

## 실행 방법

```bash
# 정답지로 테스트 (예: Q1)
cd sample/q1
cp q1_quiz_data_solution.py q1_quiz_data.py
pytest test_q1_quiz_data.py -v
```

## 의존성

Python 3.8+ (표준 라이브러리만 사용, 외부 패키지 불필요)

```
pytest
```
