# 입력 : [7, 1, 5, 3, 6, 4]
# 출력 : 5

# 최소 값일때 구매
# 최대 값일떄 판매
# 최대 - 최소 출력 (이것이 최대 이익)

list = [7, 1, 5, 3, 6, 4]

min_value = min(list)  # 최소값 저장
min_index = list[min_value]  # 최소값 인덱스 저장

print(list[min_value])  # 최소 값의 인덱스 찾기

# 반복문 실행
for i, v in enumerate(list):
    if i < min_index:  # 최소값 인덱스보다 왼쪽은 pop (이유: 최소값일때 사는게 이득이고, 그 이전의 최대는 의미가 없다.)
        list.pop(i)

# pop 으로 정리된 리스트 중 최대값 얻기
max_value = max(list)

print(max_value - min_value)

