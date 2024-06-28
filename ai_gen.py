from openai import OpenAI
import os

REPLACEMYNICK = 'REPLACEMYNICK'
BASE_TEXT = f"""Человек с ником {REPLACEMYNICK} присоединяется к голосовому чату. 
Надо перевести ник на русский язык и придумать короткое смешное кринжовое приветствие.
Требования к приветствию: 
- короткое, смешное, кринжовое;
- только одно предложение;
- не более 4-5 слов;
- без одинарных и двойных ковычек;
- ник должен быть на русском языке;
- без слова ник.
"""

def generate_greetings_text(member_nick):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': __generate_request_text__(member_nick)}
        ]
    )
    message_to_return = completion.choices[0].message.content
    print(message_to_return)
    return message_to_return

def __generate_request_text__(member_nick):
    request_text = BASE_TEXT.replace(REPLACEMYNICK, member_nick)
    print(request_text)
    return request_text