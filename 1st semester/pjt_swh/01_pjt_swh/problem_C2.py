import json
from pathlib import Path

file_path = Path('C:/Users/SSAFY/Desktop/pjt/pjt-01/도서/skeleton/data/books_500.json')

if file_path.exists() and file_path.is_file():
    with open(file_path, encoding='utf-8') as f:
        books = json.load(f)

    result = {}

    # 카테고리별 책 목록을 묶음
    for book in books:
        # category_id가 없으면 'unknown' 또는 다른 기본값을 사용
        cat_id = book.get('category_id', 'unknown')  # 'unknown'을 기본값으로 설정

        if cat_id not in result:
            result[cat_id] = {
                'name': book.get('category_name', '알 수 없음'),  # category_name도 없을 수 있어 기본값 설정
                'books': []
            }

        result[cat_id]['books'].append({
            'title': book.get('title', '제목 없음'),  # title도 없으면 기본값 설정
            'author': book.get('author', '저자 없음'),
            'publisher': book.get('publisher', '출판사 없음'),
            'pubdate': book.get('pubdate', '날짜 없음'),
            'isbn': book.get('isbn', 'ISBN 없음'),
            'price': book.get('price', '가격 없음')
        })

    # 카테고리별 책 정보 저장
    output_path = Path('category_books.json')  # 원하는 경로로 수정 가능
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"JSON 파일이 생성되었습니다: {output_path}")