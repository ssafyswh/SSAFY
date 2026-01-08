############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    result = ''     # 리스트 내 요소와 비교하기 위한 임시 결과값 생성
    count_str_len_a = 0
    for each_string in str_list:    # 리스트 내 요소들을 순회
        count_str_len_b = 0
        for _ in each_string:   # 현재 요소의 길이를 측정
            count_str_len_b += 1
        if count_str_len_a < count_str_len_b:   # 현재 요소의 길이가 현재 최대값보다 클경우 재당
            count_str_len_a = count_str_len_b
            result = each_string
    return result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(longest_string(['apple', 'banana', 'cherry', 'date']))  # 'banana'
print(longest_string(['cat', 'caterpillar', 'dog', 'elephant']))  # 'caterpillar'
print(longest_string(['a', 'ab', 'abc', 'abcd']))  # 'abcd'
#####################################################
