import random

def get_question():
    with open('question.txt', 'r', encoding='utf-8') as f:
        question_list = f.read().splitlines()
    number_question = random.randrange(0, len(question_list))
    question_answer = str(question_list[number_question])

    for i in range(0, len(question_answer)):
        if question_answer[i] == ';':
            question = question_answer[0:i]
            answer = question_answer[i + 1:len(question_answer)]
    return answer, question


# def output_question():
#     answer, question = get_question()
#     curent_view = []
#     for i in range(0, len(answer)):
#         curent_view.append('*')
#     return ''.join(curent_view)
#
#
# def answ(user):
#     answer, question = get_question()
#     curent_view = []
#     for i in range(0, len(answer)):
#         curent_view.append('*')
#     if user == answer:
#         return 'Вы правильно угадали слово!'
#     if user in answer:
#         for i in range(0, len(answer)):
#             if answer[i] == user:
#                 curent_view[i]=user
#     else:
#         return answer
#
#     return ''.join(curent_view)

if __name__ == '__main__':
    while True:
        question = input ('Введите вопрос или quit для выхода: ')
        if question == 'quit':
            break
        else:
            answer: str = input ('Введите ответ: ')
            with open('question.txt', 'a', encoding='utf-8') as f:
                f.write(question + ';' + answer + '\n')

    answer, question = get_question()
    curent_view =[]
    print(question)
    for i in range(0, len(answer)):
        curent_view.append('*')
    print(''.join(curent_view))

    while True:
        user = input ('Введите букву или назовите все слово: ')
        if user == answer:
            print('Вы правильно назвали слово!'); break
        if (user in answer):
            print('Есть такая буква!')
            for i in range (0, len(answer)):
                if answer[i] == user:
                    curent_view[i] = user
                    user_answer = ''.join(curent_view)
            if user_answer == answer:
                print('Вы правильно назвали все буквы!')
                break
        else:
            print('Такой буквы нет!')
        print(''.join(curent_view))






