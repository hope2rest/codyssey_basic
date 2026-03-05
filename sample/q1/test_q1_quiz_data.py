# test_q1_quiz_data.py  —  Q1 퀴즈 데이터 파싱 및 채점 (4 tests, 100점)
import os
import pathlib

import pytest

import q1_quiz_data as stu

QUESTION_DIR = pathlib.Path(__file__).resolve().parent


@pytest.fixture(scope="module")
def result():
    orig = os.getcwd()
    os.chdir(QUESTION_DIR)
    try:
        return stu.main()
    finally:
        os.chdir(orig)


def test_total(result):
    """[25점] 총 문항 수"""
    assert result["total"] == 5


def test_correct(result):
    """[25점] 맞힌 문항 수"""
    # user_answers = ['B','A','B','C','A'], 정답 = ['B','A','C','C','B']
    # Q1: B==B O, Q2: A==A O, Q3: B!=C X, Q4: C==C O, Q5: A!=B X → 3개
    assert result["correct"] == 3


def test_score(result):
    """[25점] 점수 (백분율)"""
    assert result["score"] == 60.0


def test_details(result):
    """[25점] 상세 결과 구조 및 값"""
    details = result["details"]
    assert len(details) == 5

    # 각 항목 키 검증
    for d in details:
        assert "id" in d
        assert "correct_answer" in d
        assert "user_answer" in d
        assert "is_correct" in d

    # 정답 여부 검증
    expected_correct = [True, True, False, True, False]
    for d, exp in zip(details, expected_correct):
        assert d["is_correct"] == exp, (
            f"문항 {d['id']}: 기대 {exp}, 결과 {d['is_correct']}"
        )
