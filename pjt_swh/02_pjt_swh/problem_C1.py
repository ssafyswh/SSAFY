import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv


# 1. [ 환경 변수 로드 ]
load_dotenv()
MY_TTBKEY = os.getenv('MY_TTBKEY')

ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

# 2. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
def fetch_books_by_topic(topic, max_results=100):
    repeat_time = 0
    if max_results > 50:
        repeat_time = 2
    else:
        repeat_time = 1

    url = ALADIN_SEARCH_URL
    book_data = []
    for i in range(repeat_time):
        params = {
            'TTBKey' : MY_TTBKEY,
            'Query' : topic,
            'MaxResults' : 50,
            'Start' : i + 1,
            'Output' : "js",
            'Version' : "20131101"
        }

        response = requests.get(url, params = params)
        temp_data = response.json()
        book_data.extend(temp_data.get('item', []))

    return book_data


# 3. '인공지능' 도서 데이터를 처리하는 함수 정의
def process_ai_books():
    # 3.1 [ '인공지능' 관련 도서 검색 ]
    # fetch_books_by_topic()을 호출하여 '인공지능' 관련 도서를 100개 수집합니다.
    ai_book_data = fetch_books_by_topic('인공지능')

    # 3.2 [ 수집된 데이터에서 가격 정보가 있는 책 필터링 및 가격순 정렬 ]
    books_on_sale_list = list()
    for book in ai_book_data:
        if book.get('priceStandard') != None:
            books_on_sale_list.append(book)

    price_sorted_ls = sorted(books_on_sale_list, key = lambda x : x['priceStandard'], reverse = True)

    # 3.3 [ 상위 10개 도서 선택 ]
    top_ten = price_sorted_ls[:10]

    # 3.4 [ 상위 10개 도서 정보 출력 ]
    print('가격이 높은 순서대로 상위 10개 도서:')
    for book in top_ten:
        idx = top_ten.index(book) + 1
        title = book.get('title')
        price = book.get('priceStandard')
        print(f'{idx}. 제목: {title}, 가격: {price}원')

    # 3.5 [ JSON 파일로 저장할 데이터 준비 ]
    # output/ai_top10_books.json 파일로 저장
    json_string = json.dumps(top_ten, ensure_ascii=False, indent=4)

    json_file = Path('output/ai_top10_books.json')
    json_file.write_text(json_string, encoding='utf-8')
    

    # 3.6 [ 완료 메시지를 출력 ]
    print("'ai_top10_books.json' 파일이 생성되었습니다.")


# 함수 실행
if __name__ == '__main__':
    process_ai_books()
