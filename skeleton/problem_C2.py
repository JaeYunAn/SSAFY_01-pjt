import json
from pathlib import Path

# 파일 경로 지정
file_path = Path('./data/books_2000.json')
output_path = Path('./data/books_by_category.json')

if file_path.exists():
    # 1. 기존 json 파일 읽기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    items = data if isinstance(data, list) else data.get('item', [])

    # 2. 카테고리별로 책 데이터를 묶을 딕셔너리 생성
    category_dict = {}

    for item in items:
        # categoryName이 없으면 "미분류"로 처리
        category = item.get("categoryName", "미분류")
        
        # 해당 카테고리가 딕셔너리에 없으면 리스트 생성
        if category not in category_dict:
            category_dict[category] = []
        
        # 카테고리 리스트에 책 정보 추가
        category_dict[category].append(item)

    # 3. 새로운 JSON 파일로 저장하기
    # 저장 경로의 디렉토리가 없으면 생성
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open('w', encoding='utf-8') as file:
        # indent=4로 보기 좋게 줄바꿈 및 들여쓰기 처리, ensure_ascii=False로 한글 깨짐 방지
        json.dump(category_dict, file, ensure_ascii=False, indent=4)

    print(f"카테고리별 정리가 완료되어 '{output_path}' 파일로 저장되었습니다.")
    print(f"총 카테고리 수: {len(category_dict)}개")