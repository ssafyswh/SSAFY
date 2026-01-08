# 단축 평가

# 1
# 준비물 1: 내용이 있는 문자열
item1 = '지도'
# 준비물 2: 내용이 있는 문자열
item2 = '나침반'
result = item1 and item2
print(f'최종적으로 챙긴 물건: {result}')
# >> 최종적으로 챙긴 물건: ??

# 2
item1 = '지도'
# 준비물 2: 내용이 없는 빈 문자열
item2 = ''
result = item1 and item2
print(f'최종적으로 챙긴 물건: "{result}"')
# >> 최종적으로 챙긴 물건: ??


# 3
# 준비물 1: 내용이 없는 빈 문자열
item1 = ''
item2 = '나침반'
result = item1 and item2
print(f'최종적으로 챙긴 물건: "{result}"')
# >> 최종적으로 챙긴 물건: ??
