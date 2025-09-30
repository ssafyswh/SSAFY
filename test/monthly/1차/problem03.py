############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, len, filter, 리스트 count 메서드 사용 시 감점
def defect_rate(results):
    pass_count = 0
    fail_count = 0  # 리스트 내 요소들의 정보를 담기 위한 변수 생성
    for result in results:
        if result == 'pass':    # 문자열이 'pass'일 경우 pass_count를 올리고
            pass_count += 1
        else:
            fail_count += 1     # 'fail'일 경우 'fail_count'를 올린다.
    rate_of_fail = fail_count / (pass_count + fail_count)
    return rate_of_fail     # 도출된 변수들을 통해 불량 비율을 계산하고 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(defect_rate(['pass', 'fail', 'pass', 'fail']))   # 0.5
print(defect_rate(['pass', 'pass']))                   # 0.0
print(defect_rate(['fail', 'fail', 'fail']))           # 1.0
#####################################################