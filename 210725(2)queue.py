#%% Queue

# Queue : 일이 처리되기를 기다리는 리스트
# 목록 혹은 리스트에서 접근이 양쪽에서 가능한 구조
# FIFO (First-In, First-Out) 기본원리
# 대표적 함수 : put, peek, get
# put : 가장 나중에 쌓기
# peek : 가장 먼저 들어간 데이터 확인하기
# get : 가장 먼저 들어간 데이터 추출하기
# 자료구조 구현방법 : 직접 구현, 이미 구현된 클래스 import, List를 스택으로 구현


#%% Queue 직접 구현

# List를 갖고있는 class 선언, 이름은 Queue
# 데이터를 넣을 함수 put 정의, List의 append 함수 이용
# peek 정의, 가장 앞의 데이터를 보기 위해 인덱스 값 0 이용
# pop 함수에 파라미터 설정, 가장 앞의 데이터를 추출하기 위해 인덱스 값 0 이용
class Queue(list):
    put = list.append
    def peek(self):
        return self[0]
    def get(self):
        return self.pop(0)

# 위에서 구현한 Queue 클래스를 q라고 선언하기
q = Queue()

# q에 put 함수로 1,5,10 넣기
q.put(1)
q.put(5)
q.put(10)

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [1, 5, 10]

# get 함수로 데이터 추출하기
print("removed value is : ", q.get())           # removed value is :  1

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [5, 10]

# peek 함수로 데이터 확인하기
print("peeked value is : ", q.peek())           # peeked value is :  5

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [5, 10]


#%% Queue 클래스 import

# Queue 클래스를 import 하기, 클래스 직접 구현 없이 Queue 선언 가능
from queue import Queue

# 위에서 구현한 Queue 클래스를 q라고 선언하기
q = Queue()

# q에 put 함수로 1,5,10 넣기
q.put(1)
q.put(5)
q.put(10)

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [1, 5, 10]

# get 함수로 데이터 추출하기
print("removed value is : ", q.get())           # removed value is :  1

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [5, 10]

# peek 함수로 데이터 확인하기
print("peeked value is : ", q.peek())           # peeked value is :  5

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [5, 10]


#%% List를 Queue로 활용

# Queue로 활용될 list의 이름을 q로 정하기
q = []

# List의 append 함수로 1,5,10 입력하기
q.append(1)
q.append(5)
q.append(10)

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [1, 5, 10]

# pop 함수에 파라미터 설정, 첫번째 데이터를 추출하기 위해 인덱스 값 0 이용
print("removed value is : ", q.pop(0))          # removed value is :  1

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [5, 10]

# peek 함수로 첫번째 데이터 확인하기
print("peeked value is : ", q[0])               # peeked value is :  5

# q 출력하기
print("my queue is : ", q)                      # my queue is :  [5, 10]


