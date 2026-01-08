import json
from pprint import pprint
from pathlib import Path

file_path = Path('C:/Users/SSAFY/Desktop/pjt/pjt-01/도서/skeleton/data/books_20.json')  # 파일 경로 설정

if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    book_titles = []
    for item in data['item']:
        book_titles.append(item['title'])

    print("책 제목 리스트: ")
    pprint(book_titles)
else:
    print(f'파일이 존재하지 않습니다: {file_path}')