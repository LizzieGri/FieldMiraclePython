import random


def write_question(num):
    count = 0
    while count < num:
        question = input("Введите вопрос: ")
        answer = input("Введите правильный ответ на вопрос: ")
        count += 1

        with open('question.txt', 'a', encoding = 'utf-8') as f:
            f.write(question + ';' + answer + '\n')


def get_question():
    with open('question.txt', 'r', encoding = 'utf-8') as f:
        question_list = f.read().splitlines()
    number_question = random.randrange(0, len(question_list))
    question_answer = str(question_list[number_question])

    for i in range(0, len(question_answer)):
        if question_answer[i]==';':
            question = question_answer[0:i]
            answer = question_answer[i+1:len(question_answer)]

    return answer

