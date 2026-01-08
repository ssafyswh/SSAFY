############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):
    max_value = 0
    max_position_x = 0
    max_position_y = 0 # 최대값과 그 좌표를 저장할 변수 생성
    for y in range(len(matrix)): 
        for x in range(len(matrix[y])): # 2중 for문으로 각 좌표에 있는 요소를 순회
            if matrix[y][x] > max_value: # 현재 최대값보다 순회중인 요소의 값이 클 경우
                max_value = matrix[y][x] 
                max_position_x = x
                max_position_y = y  # 최대값과 좌표에 현재 요소의 값과 좌표를 할당
    return [max_position_x, max_position_y] # 최종 최대값의 좌표를 반환      



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
