import json
from pathlib import Path

# 파일 경로 지정
file_path = Path('./data/books_2000.json')
output_path = Path('./data/series.json')

if file_path.exists():
    # 1. 기존 books_2000.json 파일 읽기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    items = data if isinstance(data, list) else data.get('item', [])

    # 2. 시리즈별로 책들을 그룹화할 딕셔너리 생성
    series_dict = {}

    for item in items:
        # seriesInfo 속성이 존재하고 내부 데이터가 있는지 확인
        series_info = item.get('seriesInfo')
        
        if series_info and isinstance(series_info, dict):
            # 시리즈 이름(seriesName) 가져오기
            series_name = series_info.get('seriesName')
            
            # seriesName이 존재하는 경우에만 묶기
            if series_name:
                if series_name not in series_dict:
                    series_dict[series_name] = []
                
                series_dict[series_name].append(item)

    # 3. 새로운 series.json 파일로 저장하기
    output_path.parent.mkdir(parents=True, exist_ok=True)  # 폴더가 없으면 생성

    with output_path.open('w', encoding='utf-8') as file:
        # 한글 깨짐 방지(ensure_ascii=False) 및 들여쓰기(indent=4) 적용
        json.dump(series_dict, file, ensure_ascii=False, indent=4)

    print(f"시리즈 정보 추출 완료! '{output_path}'에 저장되었습니다.")
    print(f"총 {len(series_dict)}개의 시리즈가 정리되었습니다.")