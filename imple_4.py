# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤 그 뒤에 모든 숫자를 더한 값을 이어서 출력
# ex) K1KA5CB7 --> ABCKK13

# 해결 아이디어 : 문자열을 하나씩 확인하며 숫자는 합계, 알파벳은 리스트에 저장

from unittest import result


input_data = input()
value = 0
result = []

for i in input_data:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
