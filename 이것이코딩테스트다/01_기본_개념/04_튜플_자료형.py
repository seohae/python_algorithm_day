# 튜플 자료형
# 리스트와 유사하지만 튜플은 한번 선언된 값을 변경할 수 없다. 소괄호()를 사용한다.
# 리스트에 비해 상대적으로 공간 효율적이다. (더 적은 양의 메모리를 사용한다.)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[3])  # 4
print(a[1:4])  # (2, 3, 4)

# 불가능: a[2] = 7


"""
튜플을 사용하면 좋은 경우
1) 서로 다른 성질의 데이터를 묶어서 관리해야할 경우 ex) (비용, 노트번호) 처럼 서로 다른 데이터 타입을 묶어서 관리해야할 때 
2) 해싱(Hashing)의 키 값으로 사용해야할 때 (변경이 불가능하므로)
3) 때리스트보다 메모리를 효율적으로 사용해야 할 
"""

