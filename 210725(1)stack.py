#%% Stack

# Stack : 쌓다
# 목록 혹은 리스트에서 접근이 한 쪽에서만 가능한 구조
# LIFO (Last-In, First-Out) 기본원리
# 대표적 함수 : push, peek, pop
# push : 위에 쌓기
# peek : 가장 위에 있는 데이터 확인
# pop : 가장 마지막에 넣은 데이터 추출하기
# 자료구조 구현방법 : 직접 구현, 이미 구현된 클래스 import, List를 스택으로 구현
# PYTHON은 List가 스택으로 사용 가능하도록 구현되어 있으므로 '직접 구현' 선택함


#%% Stack 직접 구현

# List를 가지고 있는 class를 선언하기, class 이름은 Stack
# List에서 append 함수가 push와 똑같은 역할을 함, append 함수를 push로 지정함
# peek 함수 정하기, 가장 마지막 값을 보여주는 인덱스 값 -1을 사용
# 아니면 len 함수를 사용해도 됨 return self[len(self)-1]
# pop은 list의 내장함수로 이미 존재하기 때문에 만들지 않음

class Stack(list):
    push = list.append
    def peek(self):
        return self[-1]


# Stack 선언하기, 이름은 s
s = Stack()

# push 함수로 1,5,10 쌓기
s.push(1)
s.push(5)
s.push(10)

# stack 출력하기
print("my stack is : ", s)                      # my stack is :  [1, 5, 10]

# pop 실행하기
print("popped value is : ", s.pop())            # popped value is :  10

# stack 출력하기
print("my stack is : ", s)                      # my stack is :  [1, 5]

# peek 실행하기
print("peeked value is : ", s.peek())           # peeked value is :  5

# stack 출력하기
print("my stack is : ", s)                      # my stack is :  [1, 5]


#%% List를 활용해 Stack 구현

# Stack으로 활용될 list의 이름을 s로 정하기
s = []

# List의 append 함수로 1,5,10 입력하기
s.append(1)
s.append(5)
s.append(10)

# stack 출력하기
print("my stack is : ", s)                      # my stack is :  [1, 5, 10]

# python 내장함수 pop 실행하기
print("popped value is : ", s.pop())            # popped value is :  10

# stack 출력하기
print("my stack is : ", s)                      # my stack is :  [1, 5]

# 인덱스 값을 활용해서 마지막 값 불러오기
print("peeked value is : ", s[-1])              # peeked value is :  5

# stack 출력하기
print("my stack is : ", s)                      # my stack is :  [1, 5]

