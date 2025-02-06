import sys
import heapq

n,m,x = map(int, input().split()) # 학생과 마을수, 도로의 수(단 방향), 파티 마을 

# 인접 리스트
graph = {}
inverse_graph = {}

for _ in range(m):
    s,e,w = map(int, input().split()) # 시작점, 끝점, 소요 시간
    
    # 정방향 인접 리스트
    if s not in graph:
        graph[s] = [(w,e)]  # 소요 시간, 끝점
    else:
        graph[s].append((w,e))  # 소요 시간, 끝점

    # 역방향 인접 리스트
    if e not in inverse_graph:
        inverse_graph[e] = [(w,s)]  # 소요 시간, 시작점
    else:
        inverse_graph[e].append((w,s))  # 소요 시간, 끝점


# 특정 마을에서 마을로 가는 최단 거리들을 구하는 함수
def dijkstra(graph, town) -> dict:
    q = [] 

    # 비용 초기화
    cost_dict = {}
    for i in range(1,n+1):
        cost_dict[i] = sys.maxsize

    cost_dict[town] = 0

    heapq.heappush(q, (0,town))

    while q:
        w, node = heapq.heappop(q)

        for next_w, next_node in graph[node]:
            if cost_dict[node] + next_w < cost_dict[next_node]:
                cost_dict[next_node] = cost_dict[node] + next_w 
                heapq.heappush(q, (cost_dict[next_node], next_node))
    
    return cost_dict


if __name__ == "__main__":
    x_to_town_costs = dijkstra(graph, x) 
    town_to_x_costs = dijkstra(inverse_graph, x)

    answer = 0

    # 가장 오래 걸리는 학생 구하기
    for key in x_to_town_costs:
        cost = town_to_x_costs[key] + x_to_town_costs[key] 

        if answer < cost:
            answer = cost
    
    print(answer)