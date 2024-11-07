from openai import OpenAI
from enum import Enum
import os

import text_patterns as TextPatterns

ENV_OPEN_API_KEY = 'OPEN_API_KEY'
GPT_MODEL = 'gpt-4o-mini'
PATTERNS = Enum('Patterns', 'Greeting Cringe ACringe Banned')

def get_ai_response_text(**kwargs):
    client = OpenAI(api_key=os.getenv(ENV_OPEN_API_KEY))
    request_text = __generate_request_text__(**kwargs)
    completion = client.chat.completions.create(
        model=GPT_MODEL,
        messages=kwargs.get('reqs_history', []) + [
            {'role': 'user', 'content': request_text}
        ]
    )
    completion.choices
    message_to_return = completion.choices[0].message.content.strip('"')
    print(message_to_return)
    return request_text, message_to_return

def __generate_request_text__(**kwargs):
    if kwargs['pattern'] == PATTERNS.Greeting:
        member_nick = kwargs['member_nick']
        text_request = TextPatterns.GREETING_PATTERN.replace(TextPatterns.REPLACEMYNICK, member_nick)
    if kwargs['pattern'] == PATTERNS.Banned:
        member_nick = kwargs['member_nick']
        text_request = TextPatterns.BANNED_PATTERN.replace(TextPatterns.REPLACEMYNICK, member_nick)
    if kwargs['pattern'] == PATTERNS.Cringe:
        extra_req_data = kwargs.get('data', None)
        text_request = TextPatterns.CRING_PATTERN.replace(TextPatterns.REPLACEEXTRADATA, '') \
            if not extra_req_data else TextPatterns.CRING_PATTERN.replace(TextPatterns.REPLACEEXTRADATA, extra_req_data)
    if kwargs['pattern'] == PATTERNS.ACringe:
        extra_req_data = kwargs.get('data', None)
        text_request = TextPatterns.ACRING_PATTERN.replace(TextPatterns.REPLACEEXTRADATA, '') \
            if not extra_req_data else TextPatterns.ACRING_PATTERN.replace(TextPatterns.REPLACEEXTRADATA, extra_req_data)
    print(text_request)
    return text_request