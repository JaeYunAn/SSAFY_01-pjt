import json
from pathlib import Path

# 파일 경로 지정
file_path = Path('./data/books_2000.json')

# 1. 월별 데이터를 담을 딕셔너리 생성 (book_1 ~ book_12)
book_months = {f"book_{i}": [] for i in range(1, 13)}

if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    # books_2000.json 데이터를 리스트로 가져오기
    items = data if isinstance(data, list) else data.get('item', [])

    # 2. 월별 데이터 분류
    for item in items:
        pub_date_str = item.get("pubDate", "")
        if pub_date_str:
            try:
                # "YYYY-MM-DD" 형태에서 '월(month)' 번호만 추출
                month = int(pub_date_str.split('-')[1])
                key = f"book_{month}"
                book_months[key].append(item)
            except (IndexError, ValueError):
                continue

# 3. 월별 권수 및 평균 가격만 출력
for i in range(1, 13):
    key = f"book_{i}"
    books = book_months[key]
    
    if books:
        # priceStandard(정가) 기준 평균 가격 계산
        total_price = sum(book.get('priceSales', 0) for book in books)
        avg_price = total_price / len(books)
        print(f"{i}월 : 평균 가격: {avg_price:.2f}원 (총 {len(books)}권)")
    else:
        print(f"파일이 존재하지 않습니다: {file_path}")
