# Q3. Git 시뮬레이터 구현 (Q2 결과 활용)

| 난이도 | 권장 시간 | 배점 |
|--------|----------|------|
| ★☆☆ | 15분 | 100점 |

---

## 문제

Git의 핵심 동작(add, commit, push, pull)을 파이썬 클래스로 시뮬레이션하세요.

Q2에서 만든 퀴즈 결과(`data/quiz_results.json`)를 로드한 뒤, Git 시뮬레이터로 파일을 커밋하고 푸시/풀하는 시나리오를 실행합니다.

---

## Git 개념 정리

| 동작 | 설명 |
|------|------|
| **add** | 파일을 스테이징 영역에 올립니다. 커밋 대상을 선택하는 단계입니다. |
| **commit** | 스테이징된 파일들을 묶어 로컬 저장소에 하나의 기록(커밋)으로 저장합니다. 커밋 후 스테이징 영역은 비워집니다. |
| **push** | 로컬에만 있는 커밋을 원격 저장소에 업로드합니다. 이미 원격에 있는 커밋은 다시 보내지 않습니다. |
| **pull** | 원격 저장소의 커밋을 로컬로 가져옵니다. 이미 로컬에 있는 커밋은 다시 받지 않습니다. |

---

## 요구사항

### 1. GitRepository 클래스

- `__init__(self)`:
  - `staged_files`: 빈 리스트 (스테이징 영역)
  - `local_commits`: 빈 리스트 (로컬 커밋 이력)
  - `remote_commits`: 빈 리스트 (원격 커밋 이력)

- `add(self, filename)`:
  - 파일명을 staged_files에 추가합니다.
  - 이미 스테이징된 파일은 중복 추가하지 않습니다.

- `commit(self, message)`:
  - staged_files가 비어 있으면 `None`을 반환합니다.
  - 커밋 딕셔너리를 생성합니다: `{"id": 커밋번호, "message": 메시지, "files": 파일목록}`
  - `id`는 `len(self.local_commits) + 1` (1부터 시작)
  - 커밋을 local_commits에 추가합니다.
  - staged_files를 빈 리스트로 초기화합니다.
  - 생성한 커밋 딕셔너리를 반환합니다.

- `push(self)`:
  - local_commits 중 remote_commits에 없는 커밋을 remote_commits에 추가합니다.
  - 비교 기준은 커밋의 `id` 값입니다.
  - 새로 푸시된 커밋 리스트를 반환합니다.

- `pull(self, incoming_commits)`:
  - incoming_commits(리스트) 중 local_commits에 없는 커밋을 local_commits에 추가합니다.
  - 비교 기준은 커밋의 `id` 값입니다.
  - 새로 풀된 커밋 리스트를 반환합니다.

- `status(self)`:
  - 아래 형식의 딕셔너리를 반환합니다.

```python
{
    "staged_files": [...],         # 현재 스테이징된 파일 목록
    "local_commit_count": 정수,    # 로컬 커밋 수
    "remote_commit_count": 정수,   # 원격 커밋 수
    "unpushed_count": 정수         # 아직 푸시되지 않은 로컬 커밋 수
}
```

### 2. main()

아래 시나리오를 순서대로 실행하고 결과를 반환합니다:

```
1. quiz_results.json 로드
2. GitRepository 생성
3. "quiz_data.csv"와 "quiz_game.py"를 add → commit("Add quiz data and game")
4. "quiz_results.json"을 add → commit("Add quiz results")
5. push()
6. 동료의 커밋 pull:
   [{"id": 100, "message": "Add score feature", "files": ["score.py"]},
    {"id": 101, "message": "Fix quiz bug", "files": ["quiz_game.py"]}]
7. "README.md"를 add → commit("Add README")
8. status() 호출
```

---

## 출력 형식

```python
{
    "quiz_title": "문자열",
    "quiz_score": 실수,
    "total_local_commits": 정수,
    "total_remote_commits": 정수,
    "unpushed_count": 정수,
    "pushed_count": 정수,
    "pulled_count": 정수
}
```

---

## 채점 기준 (4항목, 각 25점)

| 항목 | 검증 내용 |
|------|----------|
| commit 동작 | 스테이징 → 커밋 → 스테이징 초기화 검증 |
| push 동작 | 로컬 → 원격 전송, 원격 커밋 수 검증 |
| pull 동작 | 외부 커밋 수신, 로컬 커밋 수 검증 |
| main() 결과 | 전체 시나리오 실행 후 상태 검증 |
