# sql 기본 및 활용 
correct_answers = "41331213314444332421411424123324344324223141411213"

user_answers = input("정답을 입력하세요: ")

wrong_indices = [i + 1 for i, (ca, ua) in enumerate(zip(correct_answers, user_answers)) if ca != ua]

print(f"틀린 개수: {len(wrong_indices)}개")
print(f"틀린 문제 번호: {wrong_indices}")