import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 1. 파일 경로 설정 (books_500.json 사용)
file_path = Path('C:/Users/SSAFY/Desktop/pjt/pjt-01/도서/skeleton/data/books_500.json')  # 파일 경로 설정 부분

# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우
    # 2. 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)  # 파일을 열고 JSON 데이터를 읽는 코드 (파일 열기, json.load 사용)

    # 3. 카테고리별 통계 집계
    category_stats = {}  # 카테고리별 통계를 저장할 딕셔너리
    for book in data:
        category_stats[book['categoryName']] = [0, 0]
    for book in data:
        category_stats[book['categoryName']][0] += 1  # 카테고리별로 도서 수와 가격을 집계하는 코드
        category_stats[book['categoryName']][1] += book['priceSales']
    # 4. 결과 출력
    print("카테고리별 도서 통계:")
    for category, stats in category_stats.items():  # 각 카테고리별 통계 출력
        print('%s: %d권, 평균 가격 %.2f원' % (category, stats[0], (stats[1] / stats[0])))
        pass  # 도서 수와 평균 가격을 출력하는 코드
else:
    print(f"파일이 존재하지 않습니다: {file_path}")
