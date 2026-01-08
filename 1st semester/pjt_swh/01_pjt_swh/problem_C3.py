import json
from pathlib import Path

def merge_series_information(input_file_path: str, output_file_name: str = 'merged_series_info.json'):
    """
    지정된 JSON 파일에서 도서 정보를 읽어 시리즈 정보를 추출하고,
    각 시리즈에 속한 책들의 정보를 병합하여 새로운 JSON 파일로 저장합니다.

    Args:
        input_file_path (str): 도서 정보가 담긴 JSON 파일의 경로입니다 (예: books_500.json).
        output_file_name (str): 병합된 시리즈 정보가 저장될 출력 JSON 파일의 이름입니다.
                                 기본값은 'merged_series_info.json'입니다.
    """
    file_path = Path(input_file_path)

    # 1. 입력 파일 존재 및 유효성 확인
    if not file_path.exists():
        print(f"오류: 지정된 파일이 존재하지 않습니다 - '{file_path}'")
        return
    if not file_path.is_file():
        print(f"오류: 지정된 경로가 파일이 아닙니다 - '{file_path}'")
        return

    # 2. JSON 파일 읽기
    try:
        with open(file_path, encoding='utf-8') as f:
            books = json.load(f)
    except json.JSONDecodeError:
        print(f"오류: JSON 파일을 읽는 데 실패했습니다. 파일 내용이 유효한 JSON 형식이 아닐 수 있습니다 - '{file_path}'")
        return
    except Exception as e:
        print(f"파일을 여는 중 예상치 못한 오류 발생: {e}")
        return

    # 시리즈 정보를 저장할 딕셔너리. seriesId를 키로 사용합니다.
    # { 'seriesId': { 'seriesId': ..., 'seriesName': ..., 'books': [...] } }
    series_data = {}

    # 3. 각 책에서 시리즈 정보 추출 및 병합
    for book in books:
        # 'seriesInfo' 키가 존재하고, 그 값이 딕셔너리 형태이며 'seriesId' 키를 포함하는지 확인
        series_info = book.get('seriesInfo')
        if series_info and isinstance(series_info, dict):
            sid = series_info.get('seriesId')
            sname = series_info.get('seriesName')

            if sid is not None and sname is not None:
                # seriesId를 문자열로 변환하여 딕셔너리 키로 사용
                sid_str = str(sid)

                # 해당 시리즈 ID가 series_data에 없으면 새로운 항목 생성
                if sid_str not in series_data:
                    series_data[sid_str] = {
                        'seriesId': sid,
                        'seriesName': sname,
                        'books': []
                    }

                # 현재 책의 정보를 해당 시리즈 목록에 추가
                # .get()을 사용하여 키가 없을 경우 기본값 설정
                series_data[sid_str]['books'].append({
                    'title': book.get('title', '제목 없음'),
                    'link': book.get('link', '링크 없음'),
                    'author': book.get('author', '저자 없음'),
                    'pubDate': book.get('pubDate', '날짜 없음'), # 'pubDate' (대문자 D) 사용
                    'description': book.get('description', '설명 없음'),
                    'isbn': book.get('isbn', 'ISBN 없음'),
                    'isbn13': book.get('isbn13', 'ISBN13 없음'),
                    'priceSales': book.get('priceSales', '가격 없음') # priceSales 추가
                })

    # 4. 병합된 시리즈 정보를 새로운 JSON 파일로 저장
    # 출력 파일은 입력 파일과 동일한 디렉토리에 생성됩니다.
    output_path = file_path.parent / output_file_name
    try:
        # 딕셔너리의 values()를 리스트로 변환하여 저장
        # 이렇게 하면 JSON 파일의 최상위가 리스트가 됩니다.
        output_list = list(series_data.values())
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_list, f, ensure_ascii=False, indent=2)
        print(f"모든 시리즈 데이터가 '{output_path}' 파일로 성공적으로 병합되었습니다.")
    except Exception as e:
        print(f"JSON 파일을 저장하는 중 오류 발생: {e}")

# --- 함수 호출 예시 ---
# books_2000.json 파일의 실제 경로를 여기에 입력하세요.
merge_series_information('C:/Users/SSAFY/Desktop/pjt/pjt-01/도서/skeleton/data/books_2000.json', 'merged_series_info_2000.json')

# 만약 다른 경로의 파일을 테스트하고 싶다면 아래와 같이 변경할 수 있습니다.
# merge_series_information('data/my_books.json', 'custom_series_output.json')
