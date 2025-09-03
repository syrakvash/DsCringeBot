REPLACEMYNICK = 'REPLACEMYNICK'
REPLACEEXTRADATA = 'REPLACEEXTRADATA'
__REPLACEMEWORDSCOUNT__ = 'REPLACEMEWORDSCOUNT'

__REPLACEMEWORDSCOUNTREQ__ = f"- не более {__REPLACEMEWORDSCOUNT__} слов;"

__BASE_REQS__ = f"""
- короткое, 'токсичное', смешное, обидное, кринжовое;
- только одно предложение;
{__REPLACEMEWORDSCOUNTREQ__}
""".strip('\n')

GREETING_PATTERN = f"""
Человек с ником {REPLACEMYNICK} присоединяется к голосовому чату. 
Надо перевести ник на русский язык и придумать приветствие.
Требования к приветствию: 
{__BASE_REQS__.replace(__REPLACEMEWORDSCOUNT__, '7')}
- без одинарных и двойных ковычек;
- ник должен быть на русском языке;
- без слова ник.
"""

CRING_PATTERN = f"""
Надо сгенерировать шутку про: {REPLACEEXTRADATA}
Требования к тексту:
{__BASE_REQS__.replace(__REPLACEMEWORDSCOUNT__, '15')}
"""

ACRING_PATTERN = f"""
Ответ на запрос: {REPLACEEXTRADATA}
Требования к тексту:
{__REPLACEMEWORDSCOUNTREQ__.replace(__REPLACEMEWORDSCOUNT__, '15')}
"""

CLMBR_PATTERN = f"""
Добавь очень важное объявление к каламбуру ниже. 
Оригинальный каламбур без редактирования.
Требование к объявлению: {__BASE_REQS__.replace(__REPLACEMEWORDSCOUNT__, '5')}
Каламбур: {REPLACEEXTRADATA}
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