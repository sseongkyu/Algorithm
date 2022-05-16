# 내 코드

import collections
from collections import defaultdict


def solution(participant, completion):
    answer = ''
    par_dict = defaultdict(int)
    for i in participant:
        par_dict[i] += 1
    for j in completion:
        par_dict[j] -= 1
    # 내 코드에서 이 부분이 collections의 Counter함수를 통해 좀더 쉽고 효율적으로 코드를 작성할 수 있음

    reverse_par_dict = dict(map(reversed, par_dict.items()))
    answer = reverse_par_dict[1]
    return answer

# 다른사람 코드


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# collections의 Counter함수 사용방법 학습
    # 여러 문자열이 주어졌을 때 문자열의 개수를 딕셔너리로 저장할 수 있다
    # 빼기연산을 통해 개수만큼 차를 하여 0인 문자열은 없어지고 개수가 남는 문자열만 딕셔너리에 저장되어있다.
    # 이 문제에서 completion의 개수는 participant의 -1개이므로 마지막 하나 남은 문자열을 출력하여 풀 수 있다.
