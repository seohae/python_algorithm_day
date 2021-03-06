# 집합 자료형
# 중복을 허용하지 않고, 순서가 없다. => 존재 여부를 판단할 경우 유용하다.
# set() 함수를 사용하여 리스트/문자열을 이용해서 초기화한다.

data = set([1, 2, 3, 4, 5])
print(data)  # {1, 2, 3, 4, 5}

data = {1, 2, 3, 4, 4, 5}
print(data)  # 중복이 제거됨 {1, 2, 3, 4, 5}


# 집합 자료형의 연산
# 합집합, 교집합, 차집합이 제공된다.
a = set([1, 2, 3, 4, 5])
b = set([6, 7, 8, 9, 5])

print(a | b)
print(a & b)
print(a - b)


data = set([1, 2, 3])

# 하나의 데이터 추가
data.add(4)

# 여러 데이터 추가
data.update([5, 6])

# 데이터 삭제
data.remove(3)


# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다. (원소를 이용하여 O(1)의 시간복잡도로 조회 가능하다.)

