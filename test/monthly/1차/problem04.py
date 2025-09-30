############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, filter 사용 시 감점
def maintenance_stats(bus_list):
    maintenance_bus_num_list = []   # 점검 대상인 버스 번호를 저장할 리스트
    for bus_num in bus_list:
        if bus_num % 2 == 0:    
            maintenance_bus_num_list.append(bus_num)    # 버스 번호가 짝수인지 확인하고 리스트에 추가
    maintenance_count = 0
    maintenance_bus_num_sum = 0     # 점검 대상 리스트의 정보를 계산하기 위한 변수 생성
    for maintenance_bus_num in maintenance_bus_num_list:
        maintenance_count += 1      # 점검 대상 리스트의 항목들의 개수를 계산
        maintenance_bus_num_sum += maintenance_bus_num  # 점검 대상 리스트의 번호 합계를 계산
    return (maintenance_count, maintenance_bus_num_sum)

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(maintenance_stats([12, 7, 10, 5, 8]))      # (3, 30)
print(maintenance_stats([3, 5, 7]))              # (0, 0)
print(maintenance_stats([2, 4, 6, 8, 10, 12]))   # (6, 42)
#####################################################