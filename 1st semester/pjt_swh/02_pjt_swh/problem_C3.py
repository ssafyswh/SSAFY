import os
import requests
from pathlib import Path
from gtts import gTTS
from dotenv import load_dotenv

# 1. [ 환경 변수 로드 ]
load_dotenv()
MY_TTBKEY = os.getenv('MY_TTBKEY')
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

# 2. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
def fetch_books_by_topic(topic, max_results=10):
    url = ALADIN_SEARCH_URL
    params = {
        'TTBKey' : MY_TTBKEY,
        'Query' : topic,
        'MaxResults' : max_results,
        'Output' : "js",
        'Version' : "20131101"
    }
    response = requests.get(url, params=params)
    data = response.json()
    book_data = data.get('item', [])
    return book_data

# 3. [ 도서 정보를 텍스트 파일로 저장하는 함수 정의 ]
# 책 정보를 "제목, 저자, 소개" 형식으로 변환하여 txt 파일로 저장
def save_books_info(books, filename='output/music_books_info.txt'):
    new_file = Path('output') / 'music_books_info.txt'
    for book in books:
        title = book.get('title')
        author = book.get('author')
        intro = book.get('description')
        with new_file.open('a', encoding='utf-8') as file:
            file.write(f'제목: {title}, 저자: {author}, 소개: {intro} \n')

    print(f"{filename} 파일이 생성되었습니다.")


# 5. [ 텍스트 파일을 오디오 파일로 변환하는 함수 정의 ]
def create_audio_file(text_file, audio_file='output/music_books.mp3'):
    tts = gTTS(text=text_file, lang='ko', slow=False)
    tts.save(audio_file)
    print(f"{audio_file} 파일이 생성되었습니다.")


# 6. [ 음악 관련 도서 데이터를 처리하는 함수 정의 ]
def process_music_books():
    # 6.1 [ '음악' 주제의 도서 데이터 수집 ]
    data = fetch_books_by_topic('음악')

    # 6.2 [ 도서 정보를 텍스트 파일로 저장 ]
    save_books_info(data)
    

    # 6.3 [ 텍스트 파일을 오디오 파일로 변환 ]
    file_path = Path('output/music_books_info.txt')
    with file_path.open('r', encoding='utf-8') as file:
        text_list = file.readlines()
    text = ' '.join(text_list)
    create_audio_file(text)

    print("모든 작업이 완료되었습니다.")


# 함수 실행
if __name__ == '__main__':
    process_music_books()
