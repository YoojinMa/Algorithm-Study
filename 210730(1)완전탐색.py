#%% 탐색 : 많은 데이터 속에서 원하는 데이터 찾기
# 웹이나 문서에서 특정 문자를 찾는 것 (신용카드, 버스카드 검색)
# 종류 : 완전탐색, 이분탐색, 깊이우선탐색, 너비우선탐색, 문자열탐색, KMP, BM

#%% 완전탐색

# 완전탐색 = 브루트 포스(Brute Force)
# 가능한 모든 경우의 수를 탐색 -> 장점 : 풀리지 않는 문제가 없음 / 단점 : 효율성 최악
# trump : 카드 배열
# 원하는 값 : 8

# 반복문으로 구현
# 왼쪽부터 하나씩 카드 확인, 원하는 카드가 나오면 멈춤
def solution(trump):
    for i in range(len(trump)):
           if trump[i] == 8:
               return i
           return -1


# 재귀함수 구현 (동적 계획법, 백트래킹, 탐욕법에서도 사용됨)
# loc : 현재 위치 (인덱스)
# solution 함수가 solution 함수를 호출 -> 재귀함수
# 다양하게 사용되지만 무한루프에 빠질 위험이 있어서 구현시 유의하기
def solution(trump, loc):
    if trump[loc] == 8:
        return loc
    else:
        return solution(trump, loc+1)
