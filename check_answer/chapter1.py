# 1장 데이터 모델링의 이해
correct_answers = "233232442311123214342223444223321"

user_answers = input("정답을 입력하세요: ")

wrong_indices = [i + 1 for i, (ca, ua) in enumerate(zip(correct_answers, user_answers)) if ca != ua]

print(f"틀린 개수: {len(wrong_indices)}개")
print(f"틀린 문제 번호: {wrong_indices}")
