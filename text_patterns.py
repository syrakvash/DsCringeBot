REPLACEMYNICK = 'REPLACEMYNICK'
REPLACEEXTRADATA = 'REPLACEEXTRADATA'
__REPLACEMEWORDSCOUNT__ = 'REPLACEMEWORDSCOUNT'
__BASE_REQS__ = """
- короткое, 'токсичное', смешное, обидное, кринжовое;
- только одно предложение;
- не более REPLACEMEWORDSCOUNT слов;
""".strip('\n')

GREETING_PATTERN = f"""
Человек с ником {REPLACEMYNICK} присоединяется к голосовому чату. 
Надо перевести ник на русский язык и придумать приветствие.
Требования к приветствию: 
{__BASE_REQS__.replace(__REPLACEMEWORDSCOUNT__, '5')}
- без одинарных и двойных ковычек;
- ник должен быть на русском языке;
- без слова ник.
"""

CRING_PATTERN = f"""
Надо сгенерировать злую кринжовую шутку, которая опишет: {REPLACEEXTRADATA}
Требования к тексту:
{__BASE_REQS__.replace(__REPLACEMEWORDSCOUNT__, '15')}
"""

BANNED_PATTERN = f"""
Человек с ником {REPLACEMYNICK} забанен в голосовом чате. 
Надо перевести ник на русский язык и придумать злую кринжовую шутку, что этот человек забанен.
Требования к шутке: 
{__BASE_REQS__.replace(__REPLACEMEWORDSCOUNT__, '5')}
- без одинарных и двойных ковычек;
- ник должен быть на русском языке;
- без слова ник.
"""