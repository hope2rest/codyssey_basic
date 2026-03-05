import json


def load_json(filepath):
    """JSON 파일을 읽어 파이썬 객체를 반환한다."""
    # TODO: json 모듈로 파일 읽기
    pass


class GitRepository:
    """Git 저장소의 add, commit, push, pull 동작을 시뮬레이션하는 클래스"""

    def __init__(self):
        # TODO: staged_files(빈 리스트), local_commits(빈 리스트), remote_commits(빈 리스트) 초기화
        pass

    def add(self, filename):
        """파일을 스테이징 영역에 추가한다. 중복은 무시한다."""
        # TODO: 구현
        pass

    def commit(self, message):
        """스테이징된 파일들을 커밋한다. 스테이징이 비어 있으면 None 반환."""
        # TODO: 커밋 딕셔너리 생성 {"id": ..., "message": ..., "files": ...}
        # TODO: local_commits에 추가, staged_files 초기화
        pass

    def push(self):
        """로컬의 새 커밋을 원격에 업로드한다."""
        # TODO: remote_commits에 없는 로컬 커밋을 원격에 추가
        pass

    def pull(self, incoming_commits):
        """외부 커밋을 로컬로 가져온다."""
        # TODO: local_commits에 없는 커밋을 로컬에 추가
        pass

    def status(self):
        """저장소 상태를 반환한다."""
        # TODO: staged_files, local_commit_count, remote_commit_count, unpushed_count
        pass


def main():
    quiz_results = load_json("data/quiz_results.json")

    repo = GitRepository()

    # TODO: 시나리오 실행 (문제 설명 참고)
    # 1. "quiz_data.csv", "quiz_game.py" add → commit
    # 2. "quiz_results.json" add → commit
    # 3. push
    # 4. 동료 커밋 pull
    # 5. "README.md" add → commit
    # 6. status 확인 후 결과 반환

    return None


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
