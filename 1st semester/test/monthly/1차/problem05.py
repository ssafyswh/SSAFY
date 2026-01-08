############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 sum, map 사용 시 감점

def calc_total(price_map, orders):
    price_sum = 0   # 가격의 합계를 담기 위한 변수
    for order in orders:
        price_sum += price_map[order] # key에 해당하는 가격을 찾고 price_sum에 더하기
    return price_sum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(calc_total({'apple': 1000, 'pear': 800}, ['pear', 'apple', 'apple']))  # 2800
print(calc_total({'pen': 1200, 'note': 1500}, [])) # 0
print(calc_total({'apple': 1000, 'orange': 900, 'grape': 1200}, ['orange', 'orange'])) # 1800
#####################################################

