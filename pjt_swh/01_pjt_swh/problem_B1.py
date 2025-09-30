import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 1. 파일 경로 설정 (books_500.json 사용)
file_path = Path('C:/Users/SSAFY/Desktop/pjt/pjt-01/도서/skeleton/data/books_500.json') # 파일 경로 설정 부분

# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우
    # 2. 파일 열기
    with file_path.open('r',encoding='utf-8') as file:
        data = json.load(file)
     # 파일을 열고 JSON 데이터를 읽는 코드 (파일 열기, json.load 사용)
    # 3. 어린이 도서가 아닌 책 필터링
    non_children_books = []  # 어린이 도서가 아닌 책을 저장할 리스트
    for book in data:
        category = book['categoryName']
        if '어린이' not in category:
            non_children_books.append((book))
            # '어린이' 카테고리가 포함되지 않은 책을 필터링하는 코드

    # 4. 결과 출력
    print("어린이 도서가 아닌 책 목록:")
    for book in non_children_books:
            print(f"{book['title']}-{book['categoryName']}")  # 도서 제목과 카테고리를 출력하는 코드
else:
    print(f"파일이 존재하지 않습니다: {file_path}")
