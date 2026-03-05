import csv


class Question:
    """퀴즈 문항 하나를 나타내는 클래스"""

    def __init__(self, id, text, options, answer):
        # TODO: 속성 초기화 (id, text, options, answer)
        pass

    def is_correct(self, user_answer):
        """사용자 답이 정답이면 True, 아니면 False"""
        # TODO: 구현
        pass


class Quiz:
    """여러 문항을 관리하고 채점하는 클래스"""

    def __init__(self, title):
        # TODO: title, questions(빈 리스트), user_answers(빈 리스트) 초기화
        pass

    def load_from_csv(self, filepath):
        """CSV 파일에서 퀴즈 데이터를 읽어 Question 객체를 생성한다.
        Q1의 load_quiz() 로직을 클래스 메서드로 재구현한다."""
        # TODO: csv.DictReader로 파일 읽기
        # TODO: 각 행을 Question 객체로 변환하여 self.questions에 추가
        pass

    def submit_answer(self, user_answer):
        """사용자 답안을 순서대로 추가한다."""
        # TODO: 구현
        pass

    def get_score(self):
        """맞힌 개수를 반환한다."""
        # TODO: 구현
        pass

    def get_results(self):
        """채점 결과 딕셔너리를 반환한다."""
        # TODO: title, total, correct, score, details를 포함하는 딕셔너리 반환
        pass


def main():
    # TODO: Quiz 객체 생성 (제목: "Python 기초")
    # TODO: load_from_csv("data/quiz_data.csv") 호출
    # TODO: 답안 제출: 'B', 'A', 'B', 'C', 'A' (Q1과 동일)
    # TODO: get_results() 반환

    return None


if __name__ == "__main__":
    import json
    print(json.dumps(main(), indent=2, ensure_ascii=False))
