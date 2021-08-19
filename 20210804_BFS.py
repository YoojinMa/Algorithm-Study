'''
BFS
Breadth First Search 너비 우선 탐색
한 경우의 수에 대한 단계의 모든 경우의 수 조사
위에서 밑으로 내려가면서 해당 단계의 모든 경우의 수를 검사함

                A
           /    |     \
        B       C       D
      / \       |       |  \
    E   F     정답      H   I
  /    / \      |     / \
J     K  L     M     N  O


A  -B-C-D  -E-F-정답  ->종료


BFS와 큐(선입선출)
위에서 밑으로 내려가면서 해당 단계의 모든 경우의 수를 큐에 추가함
A 검사중 -> B, C, D 큐에 추가
B 검사중 -> E, F 큐에 추가
C 검사중 -> 정답 큐에 추가
D 검사중 -> H, I 큐에 추가
E 검사중 -> J 큐에 추가
F 검사중 -> K, L 큐에 추가
정답 검사중 -> 종료



예) 최단 경로 찾기
1번 섬에서부터 12번 섬까지 가는 최단 경로는 얼마인가?
(단, 모든 경로의 거리는 1이다.)

(그림 생략)

[예시코드]

# 큐에 데이터가 있다면
while len(queue)>0:
    
    # 같은 거리에 있는 데이터 개수
    count = len(queue)
    
# 같은 거리에 있는 큐의 개수만큼 검사
    for time in range(count):
        now = queue.pop(0)
        
        # 정답이 존재하면 값 반환
        if now == dest:
            return answer
            
# 연결된 포인트 완전 탐색
        for i in data:
            
            # 방문하지 않은 연결된 길이라면 큐에 추가하고 방문 표시
            if i[0] == now and visited[i[1]-1] == False:
                queue.append(i[1])
                visited[i[1]-1] = True
            elif i[1] == now and visited[i[0]-1] == False:
                queue.append(i[0])
                visited[i[0]-1] = True
                
    # 거리를 1 더 벌리기
    answer += 1
    
return answer

'''
