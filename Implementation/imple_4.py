# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤 그 뒤에 모든 숫자를 더한 값을 이어서 출력
# ex) K1KA5CB7 --> ABCKK13

# 해결 아이디어 : 문자열을 하나씩 확인하며 숫자는 합계, 알파벳은 리스트에 저장

# 입력 및 초기값 설정
input_data = input()
value = 0
result = []

# 입력데이터에서 하나씩 확인하면서 result리스트에 삽임
for i in input_data:
    # 알파벳은 result에 삽임
    if i.isalpha():
        result.append(i)
    # 숫자는 따로 더함
    else:
        value += int(i)
# 알파벳이 들어있는 result리스트 정렬
result.sort()

# 숫자가 존재하면 result리스트에 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
