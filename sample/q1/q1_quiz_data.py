import csv


def load_quiz(filepath):
    """CSV 파일에서 퀴즈 데이터를 로드하여 리스트로 반환한다."""
    # TODO: csv 모듈로 파일을 읽고, 각 행을 딕셔너리로 변환
    # 반환 형식: [{'id': int, 'question': str, 'options': {'A':..,'B':..,'C':..}, 'answer': str}, ...]
    pass


def check_answers(quiz_list, user_answers):
    """퀴즈 리스트와 사용자 답안을 비교하여 채점 결과를 반환한다."""
    # TODO: 각 문항별 정답 여부를 판별하고 결과 딕셔너리를 반환
    # 반환 형식: {'total': int, 'correct': int, 'score': float, 'details': [...]}
    pass


def main():
    data_path = "data/quiz_data.csv"
    user_answers = ["B", "A", "B", "C", "A"]

    # TODO: load_quiz로 데이터 로드
    # TODO: check_answers로 채점
    # TODO: 결과 반환

    return None


if __name__ == "__main__":
    import json
    print(json.dumps(main(), indent=2, ensure_ascii=False))
