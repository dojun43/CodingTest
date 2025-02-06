import sys
import heapq

def solution(n, edge):
    answer = 0
    
    # 비용
    cost_dict = {}
    
    for i in range(1,n+1):
        cost_dict[i] = sys.maxsize
    
    # heap
    q = []
    
    # 인접 리스트
    graph = {}
    
    for vertex in edge:
        a, b = vertex[0], vertex[1]
        
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
                
    # 초기화 
    cost_dict[1] = 0 
    
    # 다익스트라
    for next_node in graph[1]:
        heapq.heappush(q, (1, 1, next_node))  # cost, node1, node2
    
    while q:
        cost, node1, node2 = heapq.heappop(q)
                
        if cost_dict[node1] + cost < cost_dict[node2]:
            cost_dict[node2] = cost_dict[node1] + cost
            
            for next_node in graph[node2]:
                heapq.heappush(q, (1, node2, next_node))  # cost, node1, node2
            
    # 멀리 떨어진 노드 개수 구하기        
    max_dist = max(cost_dict.values())
    
    for val in cost_dict.values():
        if val == max_dist:
            answer += 1 
            
    return answer