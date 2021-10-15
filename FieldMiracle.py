def write_question(num):
    count = 0
    while count < num:
        question = input("Введите вопрос: ")
        answer = input("Введите правильный ответ на вопрос: ")
        count += 1

        with open('question.txt', 'a', encoding = 'utf-8') as f:
            f.write(question + ';' + answer + '\n')




