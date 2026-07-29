from datetime import datetime  # 날짜와 시간 처리를 위한 라이브러리
import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리

# 1. 파일 경로 설정 (books_500.json 사용)
file_path = Path('./data/books_500.json')  # 파일 경로 설정 부분

# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우

# 2. 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file) # JSON 데이터를 파이썬 딕셔너리로 변환 (json.load 사용)

items = data.get('item', []) if isinstance(data, dict) else data

# 3. 출판일을 기준으로 최신 도서 10개 추출 (날짜 문자열 기준 내림차순 정렬 후 상위 10개)
# 날짜 필드 이름이 'pubDate'라고 가정할 때의 예시입니다. (데이터 구조에 따라 변경 필요)
latest_books = sorted(
    items, 
    key=lambda x: x.get('pubDate', ''), 
    reverse=True
)[:10]

# 4. 결과 출력
print("최신 도서 10개:")
for book in latest_books:  # 선택된 도서를 순회하며 출력
    title = book.get('title', '제목 없음')
    pub_date = book.get('pubDate', '출판일 모름')
    print(f"- {title} - {pub_date}")
else:
    print(f"파일이 존재하지 않습니다: {file_path}")