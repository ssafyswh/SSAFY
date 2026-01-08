from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

file_path = Path('C:/Users/SSAFY/Desktop/pjt/pjt-01/도서/skeleton/data/books_2000.json')

# 파일 존재 여부 체크
if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    monthly_prices = {month: [] for month in range(1, 13)}

    for book in data:
        pub_date = book['pubDate']
        price = book['priceSales']

        # 출판일을 날짜 객체로 변환하여 월 정보를 추출
        month = datetime.strptime(pub_date, "%Y-%m-%d").month

        # 월별 가격 목록에 가격 추가
        monthly_prices[month].append(price)

    # 월별 평균 가격 및 도서 수 출력
    print("월별 평균 가격 및 도서 수:")
    for month in range(1, 13):
        prices = monthly_prices[month]
        if prices:  # 가격 리스트가 비어 있지 않다면
            avg_price = sum(prices) / len(prices)
            print(f"{month}월: 평균 가격 {avg_price:.2f}원 (총 {len(prices)}권)")
else:
    print(f"파일이 존재하지 않습니다: {file_path}")
