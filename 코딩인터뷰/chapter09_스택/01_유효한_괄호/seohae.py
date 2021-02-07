# 괄호로 된 입력 값이 올바른지 판별하라

# 입력 ()[]{}
# 출력 true

# 리스트로 구현해보자.

list = ["(", ")", "}", "{", "]", "["]

stack = []

table = {
    ')': '(',
    '}': '{',
    ']': '['
}

# 리스트만큼 반복문 실행
result = True

for char in list:
    # table 안에 없다면 (key 체크이므로, '(' 또는 '{' 또는 '{'이 왔을때 stack 에 push 된다.)
    if char not in table:
        stack.append(char)
        # table 에 있는 key 라면, stack 이 비어져있으면 안된다.
        # 또한 char 로 가져온 table 안의 value 와 stack 의 마지막 요소를 뺀 값이 같지 않으면 안된다.
    elif not stack or table[char] != stack.pop():
        result = False
        break
