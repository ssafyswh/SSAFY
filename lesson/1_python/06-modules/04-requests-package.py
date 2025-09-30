# requests 패키지를 사용하여 웹 API로부터 데이터를 가져오는 예시 코드입니다.
# 이 코드를 실행하기 전, 터미널에 'pip install requests'를 입력하여 패키지를 설치해야 합니다.

# HTTP 요청을 보내기 위한 requests 패키지를 불러옵니다.
import requests

# 데이터를 요청할 API의 주소(URL)를 문자열로 정의합니다.
# Nager.Date API를 사용하여 2025년 대한민국의 공휴일 정보를 요청합니다.
url = "https://date.nager.at/api/v3/publicholidays/2025/KR"

# requests.get(url)을 통해 해당 URL에 GET 요청을 보냅니다.
# .json() 메서드를 사용하여 서버로부터 받은 JSON 형식의 응답(response)을
# 파이썬 딕셔너리 또는 리스트 형태로 변환하여 response 변수에 저장합니다.
response = requests.get(url).json()

# 파이썬 객체로 변환된 공휴일 정보를 화면에 출력합니다.
print(response)
