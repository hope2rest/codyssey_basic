# Q2. 퀴즈 클래스 구현 (Q1을 클래스로 리팩토링)

| 난이도 | 권장 시간 | 배점 |
|--------|----------|------|
| ★☆☆ | 10분 | 100점 |

---

## 문제

Q1에서 함수로 구현한 퀴즈 파싱/채점 로직을 **클래스(객체 지향)** 로 리팩토링하세요.

동일한 `data/quiz_data.csv`를 사용하되, Question과 Quiz 클래스로 코드를 구조화합니다.

---

## 요구사항

### 1. Question 클래스

- `__init__(self, id, text, options, answer)`:
  - `id`: 문항 번호 (int)
  - `text`: 질문 문자열
  - `options`: 보기 딕셔너리 (`{'A': '...', 'B': '...', 'C': '...'}`)
  - `answer`: 정답 문자열
- `is_correct(self, user_answer)`: 사용자 답이 정답이면 `True` 반환

### 2. Quiz 클래스

- `__init__(self, title)`:
  - `title`: 퀴즈 제목
  - `questions`: 빈 리스트
  - `user_answers`: 빈 리스트
- `load_from_csv(self, filepath)`: Q1에서 만든 CSV 파싱 로직을 활용하여 quiz_data.csv를 읽고 Question 객체를 생성하여 questions에 추가
- `submit_answer(self, user_answer)`: 답안을 user_answers에 순서대로 추가
- `get_score(self)`: 맞힌 개수(int) 반환
- `get_results(self)`: 아래 형식의 결과 딕셔너리 반환

### 3. main()

- Quiz 객체 생성 (제목: `"Python 기초"`)
- `load_from_csv("data/quiz_data.csv")` 호출
- Q1과 동일한 답안 `['B', 'A', 'B', 'C', 'A']`를 순서대로 제출
- `get_results()` 반환

---

## 출력 형식

```python
{
    "title": "문자열",
    "total": 정수,
    "correct": 정수,
    "score": 실수,          # 백분율, 소수점 1자리
    "details": [
        {
            "id": 정수,
            "question": "문자열",
            "correct_answer": "문자열",
            "user_answer": "문자열",
            "is_correct": bool
        },
        ...
    ]
}
```

---

## Q1과의 연결

- Q1에서 `load_quiz()` 함수로 작성한 CSV 파싱 로직을 `Quiz.load_from_csv()` 메서드 안에 클래스 방식으로 재구현합니다.
- 동일한 데이터, 동일한 답안이므로 채점 결과(correct=3, score=60.0)도 Q1과 동일해야 합니다.

---

## 채점 기준 (4항목, 각 25점)

| 항목 | 검증 내용 |
|------|----------|
| Question.is_correct | 정답/오답 판별 동작 |
| Quiz.load_from_csv | CSV 로드 후 문항 수 검증 |
| Quiz.get_score | 맞힌 개수 (Q1과 동일하게 3) |
| main() 결과 | 전체 결과 딕셔너리 값 검증 |
