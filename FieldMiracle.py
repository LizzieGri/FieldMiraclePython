def write_question(question, answer):
    with open('question.txt', 'a', encoding = 'utf-8') as f:
            f.write(question + ';' + answer + '\n')
    return question + ';' + answer

 
