questions = open("questions.txt", "r")

question_list = [line.strip() for line in questions]
questions.close()

score = 0
total = len(question_list)

for line in question_list:
    q, a = line.split("=")

    answer = input(f"{q}: ")

    if a == answer:
        score += 1

result = open("result.txt", "w")
result.write(f"{score}/{total}")

result.close()
