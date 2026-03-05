# test_q3_git_log.py  —  Q3 Git 시뮬레이터 (4 tests, 100점)
import os
import pathlib

import pytest

import q3_git_log as stu

QUESTION_DIR = pathlib.Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# commit 동작 단독 검증
# ---------------------------------------------------------------------------
def test_commit_behavior():
    """[25점] commit: 스테이징 → 커밋 생성 → 스테이징 초기화"""
    repo = stu.GitRepository()

    # 빈 스테이징에서 커밋하면 None
    assert repo.commit("empty") is None

    # add → commit
    repo.add("a.py")
    repo.add("b.py")
    repo.add("a.py")  # 중복 add 무시
    c = repo.commit("first commit")

    assert c is not None, "커밋이 생성되어야 합니다"
    assert c["id"] == 1
    assert c["message"] == "first commit"
    assert sorted(c["files"]) == ["a.py", "b.py"], "중복 파일 없이 2개"
    assert len(repo.staged_files) == 0, "커밋 후 스테이징이 비어야 합니다"
    assert len(repo.local_commits) == 1


# ---------------------------------------------------------------------------
# push 동작 단독 검증
# ---------------------------------------------------------------------------
def test_push_behavior():
    """[25점] push: 로컬 커밋을 원격에 업로드"""
    repo = stu.GitRepository()

    repo.add("x.py")
    repo.commit("c1")
    repo.add("y.py")
    repo.commit("c2")

    pushed = repo.push()
    assert len(pushed) == 2, "2개 커밋이 푸시되어야 합니다"
    assert len(repo.remote_commits) == 2

    # 두 번째 push는 새 커밋이 없으므로 빈 리스트
    pushed2 = repo.push()
    assert len(pushed2) == 0, "이미 푸시된 커밋은 다시 보내지 않습니다"
    assert len(repo.remote_commits) == 2


# ---------------------------------------------------------------------------
# pull 동작 단독 검증
# ---------------------------------------------------------------------------
def test_pull_behavior():
    """[25점] pull: 외부 커밋을 로컬로 가져오기"""
    repo = stu.GitRepository()

    repo.add("a.py")
    repo.commit("local commit")

    incoming = [
        {"id": 50, "message": "remote work", "files": ["r.py"]},
        {"id": 51, "message": "more work", "files": ["s.py"]},
    ]
    pulled = repo.pull(incoming)
    assert len(pulled) == 2, "2개 커밋이 풀되어야 합니다"
    assert len(repo.local_commits) == 3, "로컬 1 + 풀 2 = 3"

    # 같은 커밋 다시 pull → 중복 없음
    pulled2 = repo.pull(incoming)
    assert len(pulled2) == 0, "이미 있는 커밋은 다시 받지 않습니다"
    assert len(repo.local_commits) == 3


# ---------------------------------------------------------------------------
# main() 시나리오 전체 검증
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def result():
    orig = os.getcwd()
    os.chdir(QUESTION_DIR)
    try:
        return stu.main()
    finally:
        os.chdir(orig)


def test_main_result(result):
    """[25점] main() 전체 시나리오 결과"""
    # Q2 퀴즈 결과 로드 확인
    assert result["quiz_title"] == "Python 기초"
    assert result["quiz_score"] == 60.0

    # 로컬: commit 3개 + pull 2개 = 5
    assert result["total_local_commits"] == 5, (
        f"로컬 커밋: 기대 5, 결과 {result['total_local_commits']}"
    )
    # 원격: push 시점에 2개
    assert result["total_remote_commits"] == 2, (
        f"원격 커밋: 기대 2, 결과 {result['total_remote_commits']}"
    )
    # 미푸시: pull 2개 + 이후 commit 1개 = 3
    assert result["unpushed_count"] == 3, (
        f"미푸시: 기대 3, 결과 {result['unpushed_count']}"
    )
    assert result["pushed_count"] == 2
    assert result["pulled_count"] == 2
