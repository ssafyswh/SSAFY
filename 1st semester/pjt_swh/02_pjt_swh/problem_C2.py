import os
import requests
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# 1. [ 환경 변수 로드 ]
load_dotenv()
MY_TTBKEY = os.getenv('MY_TTBKEY')
OPENAI_API_KEY = os.getenv('MY_API_KEY')
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

# 2. OpenAI API 클라이언트 초기화
client = OpenAI(api_key=OPENAI_API_KEY)


# 3. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
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

        response = requests.get(url, params=params)
        temp_data = response.json()
        book_data.extend(temp_data.get('item', []))

    return book_data



# 4. 책 데이터를 ChatGPT로 분류하는 함수 정의 (습관, 시간관리, 독서법, 기타)
def classify_books_with_gpt(books):
    # 4.1 [ 분류할 책 제목들을 전달하기 편한 문자열로 취합 ]
    title_list = []
    for book in books:
        title_list.append(book.get('title'))
    
    text = '\n'.join(title_list)


    # 4.2 [ ChatGPT 대화 메시지 설정 (프롬프트 작성) ]
    # 습관, 시간관리, 독서법, 기타 로 분류
    conversation_history = [
        {"role": "system", "content": "당신은 도서관에서 10년째 근속하는 사서입니다. 책 제목을 보고 키워드를 기반으로 책을 분류하세요"},      # 페르소나 작성
        {"role": "system", "content": "답변은 절대 `백틱` 없이 json으로만 출력해줘 { \"습관\": [제목 1, 제목 2, ....], \"시간 관리\": [제목 1, 제목 2, ...], ...}과 같은 json 형태로 출력해줘"},
        {"role": "user",
        "content": f"다음은 '독서' 키워드로 검색하여 찾은 임의의 도서 100개의 제목 목록이야. {text} 이 책의 제목들을 모두 '습관', '시간관리', '독서법', '기타' 4가지 항목 중 하나로 분류해줘."}         # 요청 프롬프트 작성
    ]

    # 4.3 [ 생성형 AI에 분류 요청 보내기 ]
    # client.chat.completions.create() 호출 (example 코드 참고)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        max_tokens=15000,
        temperature=1.0,
        top_p = 1.0,
        n = 1,
        seed=1000
    )
    # response_list = []
    # for response in response.choices:
    #     response_list.append(response.message.content)
    # 4.4 [ ChatGPT의 응답을 가져와 JSON 으로 추출 ]
    # ! 주의. JSON 형태로 프롬프팅을 하지 못하면 파싱에서 에러가 발생할 수 있습니다.
    # classification = json.dumps(response_list, ensure_ascii=False, indent=4)
    json_text = response.choices[0].message.content
    book_dict = json.loads(json_text)
      # 응답에서 JSON 데이터를 추출하고 파싱

    return book_dict   #classification   # 분류 정보 반환


# 5. [ 데이터를 JSON 파일로 저장하는 함수 정의 ]
def save_to_json(data, filename='output/reading_habits.json'):

    book_json_string = json.dumps(data, ensure_ascii=False, indent=4)
    book_json = Path(filename)
    book_json.write_text(book_json_string, encoding= 'utf-8')


# 6. '독서' 도서 데이터를 처리하는 함수 정의
def process_reading_books():
    # 6.1 [ '독서'와 관련된 도서 검색 (100개) ]
    book_data = fetch_books_by_topic('독서')  # fetch_books_by_topic() 호출

    # 6.2 [ 생성형 AI를 이용해 책 분류 ]
    classified_book = classify_books_with_gpt(book_data)  # classify_books_with_gpt() 호출

    # 6.3 [ 분류된 책 정보를 JSON 파일로 저장 ]
    # output/reading_habits.json 으로 저장하기
    save_to_json(classified_book)  # save_to_json() 호출

    # 완료 메시지 출력
    print("'output/reading_habits.json' 파일이 생성되었습니다.")


# 함수 실행
if __name__ == '__main__':
    process_reading_books()
