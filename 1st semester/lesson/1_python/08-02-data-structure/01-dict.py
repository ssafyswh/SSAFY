# get
# person = {'name': 'Alice', 'age': 25}
# print(person.get('name'))
# print(person.get('country'))
# print(person.get('country', '해당 키는 존재하지 않습니다.'))
# print(person['name'])
# print(person['country'])  # KeyError: 'country'

# keys
# person = {'name': 'Alice', 'age': 25}
# print(person.keys())  # dict_keys(['name', 'age'])
# for key in person.keys():
#     print(key)


# values
# person = {'name': 'Alice', 'age': 25}
# print(person.values())  # dict_values(['Alice', 25])
# for value in person.values():
#     print(value)


# items
# person = {'name': 'Alice', 'age': 25}
# print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
# for key, value in person.items():
#     print(key, value)

# pop
# person = {'name': 'Alice', 'age': 25}
# print(person.pop('age'))  # 25
# print(person)  # {'name': 'Alice'}
# print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError: 'country'

# clear
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person)

# setdefault
# person = {'name': 'Alice', 'age': 25}
# print(person.setdefault('country', 'KOREA'))  # KOREA
# # print(person.setdefault('name', 'KOREA'))  # Alice
# print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL')
print(
    person
)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}





# # 똑같은 딕셔너리 유지
# D1 = {'name': 'Alice', 'age': 25}
# D1.clear()

# # 재할당 (다른 딕셔너리가 된 것)
# D2 = {'name': 'Alice', 'age': 25}
# D2 = {}
