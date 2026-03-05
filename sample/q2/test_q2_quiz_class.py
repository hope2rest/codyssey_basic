# test_q2_quiz_class.py  —  Q2 퀴즈 클래스 구현 (4 tests, 100점)
import os
import pathlib

import pytest

import q2_quiz_class as stu

QUESTION_DIR = pathlib.Path(__file__).resolve().parent


def test_question_is_correct():
    """[25점] Question.is_correct 동작 검증"""
    q = stu.Question(1, "테스트 질문", {"A": "a", "B": "b", "C": "c"}, "B")
    assert q.is_correct("B") is True
    assert q.is_correct("A") is False
    assert q.is_correct("C") is False


def test_load_from_csv():
    """[25점] Quiz.load_from_csv — CSV에서 Question 객체 로드"""
    orig = os.getcwd()
    os.chdir(QUESTION_DIR)
    try:
        quiz = stu.Quiz("테스트")
        quiz.load_from_csv("data/quiz_data.csv")
        assert len(quiz.questions) == 5, f"기대 5문항, 결과 {len(quiz.questions)}문항"
        # Question 객체 속성 확인
        q1 = quiz.questions[0]
        assert q1.id == 1
        assert q1.answer == "B"
        assert "A" in q1.options
    finally:
        os.chdir(orig)


def test_get_score():
    """[25점] Quiz.get_score — 맞힌 개수 (Q1과 동일 결과)"""
    orig = os.getcwd()
    os.chdir(QUESTION_DIR)
    try:
        quiz = stu.Quiz("테스트")
        quiz.load_from_csv("data/quiz_data.csv")
        for ans in ["B", "A", "B", "C", "A"]:
            quiz.submit_answer(ans)
        # Q1과 동일: B=B(O), A=A(O), B!=C(X), C=C(O), A!=B(X) → 3
        assert quiz.get_score() == 3
    finally:
        os.chdir(orig)


@pytest.fixture(scope="module")
def result():
    orig = os.getcwd()
    os.chdir(QUESTION_DIR)
    try:
        return stu.main()
    finally:
        os.chdir(orig)


def test_main_result(result):
    """[25점] main() 반환값 — Q1과 동일한 채점 결과"""
    assert result["title"] == "Python 기초"
    assert result["total"] == 5
    assert result["correct"] == 3
    assert result["score"] == 60.0

    # details 검증
    details = result["details"]
    assert len(details) == 5
    expected_correct = [True, True, False, True, False]
    for d, exp in zip(details, expected_correct):
        assert d["is_correct"] == exp, (
            f"문항 {d['id']}: 기대 {exp}, 결과 {d['is_correct']}"
        )
