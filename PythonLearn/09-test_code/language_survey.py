"""survey language use case"""
from survey import AnonymousSurvey

question = 'What is your usually use language?'
ano_sur = AnonymousSurvey(question)

ano_sur.show_question()
print('Enter \'q\' to quit anytime')
while True:
    responce = input('Please input your favorite language: ')
    if responce == 'q':
        break
    ano_sur.store_responce(responce)

ano_sur.show_results()
