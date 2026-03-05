import csv


def load_quiz(filepath):
    """CSV 파일에서 퀴즈 데이터를 로드하여 리스트로 반환한다."""
    quiz_list = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            quiz_list.append({
                "id": int(row["id"]),
                "question": row["question"],
                "options": {
                    "A": row["option_a"],
                    "B": row["option_b"],
                    "C": row["option_c"],
                },
                "answer": row["answer"],
            })
    return quiz_list


def check_answers(quiz_list, user_answers):
    """퀴즈 리스트와 사용자 답안을 비교하여 채점 결과를 반환한다."""
    correct = 0
    details = []
    for quiz, user_ans in zip(quiz_list, user_answers):
        is_correct = quiz["answer"] == user_ans
        if is_correct:
            correct += 1
        details.append({
            "id": quiz["id"],
            "correct_answer": quiz["answer"],
            "user_answer": user_ans,
            "is_correct": is_correct,
        })
    total = len(quiz_list)
    return {
        "total": total,
        "correct": correct,
        "score": round(correct / total * 100, 1),
        "details": details,
    }


def main():
    data_path = "data/quiz_data.csv"
    user_answers = ["B", "A", "B", "C", "A"]

    quiz_list = load_quiz(data_path)
    result = check_answers(quiz_list, user_answers)

    return result


if __name__ == "__main__":
    import json
    print(json.dumps(main(), indent=2, ensure_ascii=False))
