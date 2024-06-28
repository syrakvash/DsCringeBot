from openai import OpenAI
import os

def generate_greetings_text(text):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': text}
        ]
    )
    message_to_return = completion.choices[0].message.content
    print(message_to_return)
    return message_to_return
