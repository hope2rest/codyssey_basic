import csv


class Question:
    """퀴즈 문항 하나를 나타내는 클래스"""

    def __init__(self, id, text, options, answer):
        self.id = id
        self.text = text
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        """사용자 답이 정답이면 True, 아니면 False"""
        return self.answer == user_answer


class Quiz:
    """여러 문항을 관리하고 채점하는 클래스"""

    def __init__(self, title):
        self.title = title
        self.questions = []
        self.user_answers = []

    def load_from_csv(self, filepath):
        """CSV 파일에서 퀴즈 데이터를 읽어 Question 객체를 생성한다."""
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = Question(
                    id=int(row["id"]),
                    text=row["question"],
                    options={
                        "A": row["option_a"],
                        "B": row["option_b"],
                        "C": row["option_c"],
                    },
                    answer=row["answer"],
                )
                self.questions.append(q)

    def submit_answer(self, user_answer):
        """사용자 답안을 순서대로 추가한다."""
        self.user_answers.append(user_answer)

    def get_score(self):
        """맞힌 개수를 반환한다."""
        correct = 0
        for q, ans in zip(self.questions, self.user_answers):
            if q.is_correct(ans):
                correct += 1
        return correct

    def get_results(self):
        """채점 결과 딕셔너리를 반환한다."""
        total = len(self.questions)
        correct = self.get_score()
        return {
            "title": self.title,
            "total": total,
            "correct": correct,
            "score": round(correct / total * 100, 1) if total > 0 else 0.0,
            "details": [
                {
                    "id": q.id,
                    "question": q.text,
                    "correct_answer": q.answer,
                    "user_answer": self.user_answers[i],
                    "is_correct": q.is_correct(self.user_answers[i]),
                }
                for i, q in enumerate(self.questions)
            ],
        }


def main():
    quiz = Quiz("Python 기초")
    quiz.load_from_csv("data/quiz_data.csv")

    for ans in ["B", "A", "B", "C", "A"]:
        quiz.submit_answer(ans)

    return quiz.get_results()


if __name__ == "__main__":
    import json
    print(json.dumps(main(), indent=2, ensure_ascii=False))
