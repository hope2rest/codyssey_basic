import json


def load_json(filepath):
    """JSON 파일을 읽어 파이썬 객체를 반환한다."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


class GitRepository:
    """Git 저장소의 add, commit, push, pull 동작을 시뮬레이션하는 클래스"""

    def __init__(self):
        self.staged_files = []
        self.local_commits = []
        self.remote_commits = []

    def add(self, filename):
        """파일을 스테이징 영역에 추가한다. 중복은 무시한다."""
        if filename not in self.staged_files:
            self.staged_files.append(filename)

    def commit(self, message):
        """스테이징된 파일들을 커밋한다. 스테이징이 비어 있으면 None 반환."""
        if not self.staged_files:
            return None
        commit_data = {
            "id": len(self.local_commits) + 1,
            "message": message,
            "files": list(self.staged_files),
        }
        self.local_commits.append(commit_data)
        self.staged_files = []
        return commit_data

    def push(self):
        """로컬의 새 커밋을 원격에 업로드한다."""
        remote_ids = {c["id"] for c in self.remote_commits}
        pushed = []
        for c in self.local_commits:
            if c["id"] not in remote_ids:
                self.remote_commits.append(c)
                pushed.append(c)
        return pushed

    def pull(self, incoming_commits):
        """외부 커밋을 로컬로 가져온다."""
        local_ids = {c["id"] for c in self.local_commits}
        pulled = []
        for c in incoming_commits:
            if c["id"] not in local_ids:
                self.local_commits.append(c)
                pulled.append(c)
        return pulled

    def status(self):
        """저장소 상태를 반환한다."""
        remote_ids = {c["id"] for c in self.remote_commits}
        unpushed = [c for c in self.local_commits if c["id"] not in remote_ids]
        return {
            "staged_files": list(self.staged_files),
            "local_commit_count": len(self.local_commits),
            "remote_commit_count": len(self.remote_commits),
            "unpushed_count": len(unpushed),
        }


def main():
    quiz_results = load_json("data/quiz_results.json")

    repo = GitRepository()

    # 1. 퀴즈 파일 커밋
    repo.add("quiz_data.csv")
    repo.add("quiz_game.py")
    repo.commit("Add quiz data and game")

    # 2. 결과 파일 커밋
    repo.add("quiz_results.json")
    repo.commit("Add quiz results")

    # 3. 원격에 푸시
    pushed = repo.push()

    # 4. 동료의 커밋을 풀
    incoming = [
        {"id": 100, "message": "Add score feature", "files": ["score.py"]},
        {"id": 101, "message": "Fix quiz bug", "files": ["quiz_game.py"]},
    ]
    pulled = repo.pull(incoming)

    # 5. README 커밋
    repo.add("README.md")
    repo.commit("Add README")

    # 6. 상태 확인
    status = repo.status()

    return {
        "quiz_title": quiz_results["title"],
        "quiz_score": quiz_results["score"],
        "total_local_commits": status["local_commit_count"],
        "total_remote_commits": status["remote_commit_count"],
        "unpushed_count": status["unpushed_count"],
        "pushed_count": len(pushed),
        "pulled_count": len(pulled),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
