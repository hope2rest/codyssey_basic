# mac_scorer.py — MAC 연산 기반 패턴 매칭
# 아래 함수를 완성하세요.

import json


def load_data(filepath):
    """JSON 파일을 읽어 딕셔너리로 반환한다."""
    # TODO: json 모듈로 파일을 열어 읽기
    pass


def mac(a, b):
    """두 개의 2D 리스트에 대해 MAC(Multiply-Accumulate) 연산을 수행한다.

    같은 위치의 값을 곱한 뒤 전부 더한 값을 반환한다.
    예: a=[[1,0],[0,1]], b=[[1,0],[0,1]] → 1*1 + 0*0 + 0*0 + 1*1 = 2
    """
    # TODO: 이중 반복문으로 각 위치의 곱을 누적하여 합산
    pass


def normalize_labels(labels):
    """labels 딕셔너리의 키를 모두 소문자로 변환한 새 딕셔너리를 반환한다.

    예: {"IMG_01": "cross"} → {"img_01": "cross"}
    """
    # TODO: 각 키에 .lower()를 적용한 새 딕셔너리 생성
    pass


def is_close(a, b, epsilon=1e-6):
    """두 수의 차이가 epsilon 미만이면 True, 아니면 False를 반환한다.

    부동소수점 연산은 정확하지 않을 수 있다.
    예: 0.1 + 0.2 = 0.30000000000000004 (≠ 0.3)
    이때 is_close(0.1+0.2, 0.3) → True
    """
    # TODO: 두 수의 절대 차이와 epsilon 비교
    pass


def find_best_match(pattern, filters):
    """pattern과 각 필터의 MAC 점수를 계산하여,
    가장 높은 점수를 받은 필터 이름(str)을 반환한다."""
    # TODO: filters의 각 항목과 MAC 점수 비교 → 최고 점수 필터 이름
    pass


def main(data_path):
    """데이터를 로드하고 전체 매칭 파이프라인을 실행한다.

    반환 형식:
    {
        "scores": {"img_01": {"cross": 5, ...}, ...},
        "best_matches": {"img_01": "cross", ...},
        "labels": {"img_01": "cross_pattern", ...}
    }
    """
    # TODO: load_data로 데이터 로드
    # TODO: normalize_labels로 라벨 키 통일
    # TODO: 각 패턴 × 각 필터 MAC 점수 계산
    # TODO: 각 패턴의 최적 필터 찾기
    # TODO: 결과 딕셔너리 반환
    pass
