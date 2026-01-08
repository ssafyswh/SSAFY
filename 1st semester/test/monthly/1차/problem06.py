############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def grade_distribution(scores):
    result = {} # 등급 분류 결과를 담기 위한 딕셔너리
    for name in scores:
        if scores[name] >= 90: # 등급 구분을 위한 조건문
            if result.get('A') == None: # 해당 등급의 키가 없을 경우
                result['A'] = [name] # 그 등급에 해당하는 키에 학생 이름을 요소로 갖는 리스트를 할당
            else:
                result['A'].append(name) # 해당 등급의 키가 존재할 경우 그 값인 리스트에 학생 이름을 추가
        elif scores[name] >= 80: # 다른 등급 구간에 대해서도 반복합니다.
            if result.get('B') == None:
                result['B'] = [name]
            else:
                result['B'].append(name)
        elif scores[name] >= 70:
            if result.get('C') == None:
                result['C'] = [name]
            else:
                result['C'].append(name)
        elif scores[name] >= 60:
            if result.get('D') == None:
                result['D'] = [name]
            else:
                result['D'].append(name)
        else:
            if result.get('F') == None:
                result['F'] = [name]
            else:
                result['F'].append(name)
    return result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
case1 = {'Kim': 92, 'Lee': 75, 'Park': 88, 'Choi': 60}
# {'A': ['Kim'],  'C': ['Lee'], 'B': ['Park'], 'D': ['Choi']}
print(grade_distribution(case1))

print(grade_distribution({'Min': 95, 'Oh': 93}))       
# {'A': ['Min', 'Oh']}

case2 = {
    'Ahn': 90,   
    'Baek': 82,  
    'Choi': 75,  
    'Dong': 60,  
    'Eun': 59    
}
# {'A': ['Ahn'], 'B': ['Baek'], 'C': ['Choi'], 'D': ['Dong'], 'F': ['Eun']}
print(grade_distribution(case2))

case3 = {
    'Kim': 100,  
    'Lee': 89,   
    'Park': 70,  
    'Shin': 69,  
    'Yang': 0    
}
# {'A': ['Kim'], 'B': ['Lee'], 'C': ['Park'], 'D': ['Shin'], 'F': ['Yang']}
print(grade_distribution(case3))
#####################################################