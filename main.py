import numpy as np
from function import *
q1 = question("나이가 어떻게 되나요?\n1. 만 19세 미만\n2. 만 19세 이상\n3. 중년 이상")
q2 = question("불건전한 취미(ex. 도박 성매매)를 꺼려하시나요?\n1. 네\n2. 보통\n3. 아니요")
q3 = question("취미생활에 돈을 투자해야한다면 마지노선은 어디까지 인가요?\n1. 0~10만\n2. 10만~500만\n3. 500만~")
q4 = question("취미 생활의 깊이는 어느정도가 적당한가요?\n1. 가볍게 즐길\n2. 아무거나\n3. 하드코어")
question = [q1, q2, q3, q4]
for a in question:
    q = input(a.que)
    a.answer(select(q))
que_result = np.array([q1.ans, q2.ans, q3.ans, q4.ans])
sports = {}
sports["golf"] = favorite([-1, 0, 0, 1])
sports["billiard"] = favorite([0, 1, -1, 0])
sports["gunfire"] = favorite([0,- 1, 0, 1])
sports["hiking"] = favorite([1, 1, -1, 0])
fav_result = [sports["golf"], sports["billiard"], sports["gunfire"], sports["hiking"]]
li=[]
for a in fav_result:
    score = np.sum(np.multiply(a.pre, que_result))
    li.append(score)
print(li)