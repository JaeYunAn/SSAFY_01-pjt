"""
06_JSON_read.py
주제: JSON 파일 읽고 파이썬 객체로 변환 (json.loads / json.load)
사전 준비 : 'sample_data/' 폴더에 'books_20.json' 필요
None / _____ 로 표시된 부분을 채워봅니다.
"""

import json
from pathlib import Path


json_file = Path('sample_data/books_20.json')

# 1) loads : 파일을 '문자열'로 읽은 뒤 dict 로 변환
json_text = json_file.read_text(encoding='utf-8')
print(type(json_text))  # <class 'str'>

# [힌트] '문자열'을 파이썬 객체로 바꾸는 json 메서드는? (s = string)
data = json.loads(json_text)  # TODO
print(type(data))       # <class 'dict'>


# 2) load : 파일 객체를 그대로 변환
with json_file.open(encoding='utf-8') as f:
    # [힌트] '파일 객체'를 파이썬 객체로 바꾸는 json 메서드는?
    data = json.load(f)  # TODO
    print(type(data))     # <class 'dict'>
