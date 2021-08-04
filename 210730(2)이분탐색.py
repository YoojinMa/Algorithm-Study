#%% 이분탐색

# UPDOWN 게임 1~1000 -> 500, 750... 절반으로 범위를 줄여나감
# 이분탐색 = 이진검색
# 오름차순으로 정렬된 리스트에서 특정 값의 위치를 찾기
# 중간값을 선택해서 찾고자 하는 값과의 크고 작음을 비교함
# 정렬된 리스트를 필요로 함

# trump : 카드 배열
# 원하는 값 : 8
# left : 첫번째 위치 = [0]
# right : 마지막 위치 = 가장 큰 인덱스 값
# mid : left와 right의 중간값

# 찾고자 하는 값이 mid값보다 크면 left를 mid값+1로 새로 지정하기
# 새로운 left와 기존 right의 중간값으로 mid값 새로 지정
# 원하는 카드와 mid값이 일치할 때까지 위를 반복하기
# 찾고자 하는 값이 mid값보다 작으면 right를 mid값-1로 새로 지정하기
# 기존 left와 새로운 right의 중간값으로 mid값 새로 지정
# 원하는 카드와 mid값이 일치할 때까지 위를 반복하기

# 이분탐색 에시코드
def solution(trump):
    left = 0
    right = len(trump) - 1
    while(left <= right):
        mid = (left+right)//2
        if trump[mid] == 8:
            return mid
        elif trump[mid] < 8:
            left = mid + 1
        elif trump[mid] > 8:
            right = mid - 1
        return mid
