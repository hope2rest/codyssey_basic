## 문항 1: MAC 연산 기반 패턴 매칭

### 시험 정보
- 과정: AI 올인원
- 단계: AI·SW 기초
- 난이도: 1
- 권장 시간: 15분
- Pass 기준: 정답 체크리스트 9개 전체 충족 (100점)

### 배경 지식

**MAC(Multiply-Accumulate) 연산**은 AI의 가장 기본적인 연산입니다.
두 배열의 같은 위치 값을 곱한 뒤 모두 더하면 **유사도 점수**가 됩니다.
점수가 높을수록 두 패턴이 비슷하다는 뜻입니다.

```
패턴:   [[1, 0],    필터:   [[1, 0],
         [0, 1]]             [0, 1]]

MAC = (1×1) + (0×0) + (0×0) + (1×1) = 2  ← 완전 일치!
```

### 문제

`data/data.json`에 3×3 크기의 패턴과 필터가 저장되어 있습니다.
각 패턴이 어떤 필터와 가장 유사한지 MAC 연산으로 판별하는 프로그램을 작성하세요.

#### data.json 구조

| 키 | 내용 |
|----|------|
| `patterns` | 판별 대상 이미지 3개 (3×3 정수 배열) |
| `filters` | 비교 기준 필터 3개 (3×3 정수 배열) |
| `labels` | 패턴별 정답 라벨 (키 대소문자가 불규칙: `IMG_01`, `Img_02`, `img_03`) |

> **주의**: `labels`의 키가 `patterns`의 키와 대소문자가 다릅니다. 키를 소문자로 통일(정규화)해야 올바르게 매칭됩니다.

---

### 구현 요구사항

#### 1. `load_data(filepath)` → dict
- JSON 파일을 읽어 딕셔너리로 반환합니다.

#### 2. `mac(a, b)` → int 또는 float
- 두 개의 2D 리스트에 대해 MAC 연산을 수행합니다.
- 같은 위치의 값을 곱한 뒤 전부 더합니다.

```
mac([[1,0],[0,1]], [[1,0],[0,1]]) → 2
```

#### 3. `normalize_labels(labels)` → dict
- 딕셔너리의 키를 모두 소문자로 변환한 새 딕셔너리를 반환합니다.
- 값은 변경하지 않습니다.

```
normalize_labels({"IMG_01": "cross"}) → {"img_01": "cross"}
```

#### 4. `is_close(a, b, epsilon=1e-6)` → bool
- 두 수의 차이가 epsilon 미만이면 `True`를 반환합니다.
- 부동소수점 연산에서는 `0.1 + 0.2 == 0.3`이 `False`가 될 수 있습니다. 이를 안전하게 비교하는 함수입니다.

#### 5. `find_best_match(pattern, filters)` → str
- 패턴과 각 필터의 MAC 점수를 계산하여, 가장 높은 점수를 받은 필터 이름을 반환합니다.

#### 6. `main(data_path)` → dict
- 위 함수들을 조합하여 전체 파이프라인을 실행합니다.

---

### 출력 형식

```python
{
    "scores": {
        "img_01": {"cross": 5, "block": 2, "line": 1},
        "img_02": {"cross": 2, "block": 4, "line": 2},
        "img_03": {"cross": 1, "block": 2, "line": 3}
    },
    "best_matches": {
        "img_01": "cross",
        "img_02": "block",
        "img_03": "line"
    },
    "labels": {
        "img_01": "cross_pattern",
        "img_02": "block_pattern",
        "img_03": "line_pattern"
    }
}
```

### 제약 사항
- **외부 라이브러리 사용 금지** — `json`만 허용, 그 외 import 금지
- Python 기본 문법(반복문, 조건문, 딕셔너리)만으로 구현하세요

### 제출 방식
- `mac_scorer.py` 파일 1개를 제출합니다.
- `template/mac_scorer.py`의 빈 구현(`pass`)을 채우세요.
