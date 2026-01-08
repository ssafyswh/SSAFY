# 함수 정의
def make_sum(pram1, pram2): 
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    result = pram1 + pram2
    return result

# 함수 호출 및 반환 값 할당
sum_result = make_sum(100, 30)
# print(sum_result)


# print() 함수는 반환값이 없다.
return_value = print(1)
print(return_value)
